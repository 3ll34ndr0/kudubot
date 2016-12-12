# coding=utf-8
import re
import random
import string
from kudubot.logger.PrintLogger import PrintLogger
from kudubot.config.LocalConfigChecker import LocalConfigChecker
import os
import sqlite3

from kudubot.servicehandlers.Service import Service
from kudubot.connection.generic.Message import Message
from kudubot.servicehandlers.Authenticator import Authenticator
import sys
sys.path.append('/home/lean/arena/10cur4')
sys.path.append('/home/lean/arena/flappointment')
from app import db
from app.tables import *
import parsedatetime as pdt
import pytz
from datetime import datetime, timedelta
tz = "America/Argentina/Cordoba" #TODO: Avoid hardcoded values
from pytz import country_timezones
import locale
locale.setlocale(locale.LC_ALL,'es_AR.utf8')


# Guardo aca algunos métodos de pytz pa no olvidarme.
# country_timezones('ar') tira una lista de los horarios de cada pais, en este caso Argentina.
#horarioCordoba = pytz.timezone('America/Argentina/Cordoba')
#horarioCordoba.zone

from manager import ManageAppointments
CREDITS = [
        {
                    'name': 'address',
                    'message': 'Enviame el contacto a quien se le darán los créditos'
                },
                {
                    'name': 'credits',
                    'message': 'Por favor ingrese la cantidad de créditos que desea otorgar',
                    'required': False
                },
                {
                    'name': 'activity',
                    'message': 'Para qué actividad serán los créditos?',
                },
#                {
#                    'name': 'place',
#                    'message': 'Please send me the place of event (or /skip)',
#                            'required': False
#                },
                ]
class AppointmentService(Service):
    """
    Approintments service
    """

    identifier = "appointment"
    """
    The identifier for this service
    """

    help_description = {"en": "/appointment\t creates,reserves,modify,erasee an activity\n"
                              "syntax:\n"
                              "/appointment new activityName 10/24/16 12:30h",
                        "es": "/turno \tCrea, reserva, modifica o borra una actividad\n"
                              "Ejemplo de uso:\n"
                              "/turno nuevo nombreActividad 24/10/16 12:30"}
    """
    Help description for this service.
    """

    appointment = {"appointment": "en",
                   "turno"      : "es",
                   "turnos"     : "es",
                   "reservar"   : "es",
                   "borrar"     : "es",
                   "cancelar"   : "es",
                   "prepago"    : "es",
                   "reservas"   : "es",
                   "reserva"    : "es",
                   "asistencias": "es",
                   "asistencia" : "es"}

    """
    Keywords for the appointment command
    """

    def process_message(self, message: Message) -> None:
        """
        Process a message according to the service's functionality

        :param message: the message to process
        :return: None
        """
        # Get the phonenumber if using what the fuck:
        if self.connection.identifier == 'whatsapp':
            address = message.get_individual_address()
        else:
            address = message.get_individual_address()
            pass
            #TODO: Take into account Telegram ...
        userInput = message.message_body.lower()
        if userInput == 'turnos':
            #Should give info about appointments for today and tomorrow...
            language = userInput
            reply = str(self.giveInfo(address))
        elif userInput.split(" ",1)[0] == 'turnos': # TODO:Avoid hardcoded Language
            language, date = userInput.split(" ",1)
            reply = str(self.giveInfo(address, date,"1"))
        elif userInput == 'reserva': # TODO:Avoid hardcoded Language
            language = userInput
            reply = self.booked(address)
        elif userInput == 'reservas': # TODO:Avoid hardcoded Language
            language = userInput
            reply = self.booked(address)
        elif userInput == 'asistencias': # TODO:Avoid hardcoded Language
            language = userInput
            reply = self.attended(address)
        elif userInput == 'asistencia': # TODO:Avoid hardcoded Language
            language = userInput
            reply = self.attended(address)
        elif userInput.split(" ", 2)[1] == 'nuevo':# TODO:Avoid hardcoded Language
            language, _, activity, dayMonthYear_Hour = userInput.split(" ", 3)
            reply = self.createAppointment(activity,
                                           self.datetimeConvert(dayMonthYear_Hour),
                                           address, prePay=False)
        elif userInput.split(" ", 2)[1] == 'prepago':# TODO:Avoid hardcoded Language
            language, _, activity, dayMonthYear_Hour = userInput.split(" ", 3)
            reply = self.createAppointment(activity,
                                           self.datetimeConvert(dayMonthYear_Hour),
                                           address, prePay=True)
        elif userInput.split(" ", 2)[0] == 'borrar':
            print("DEBUG: {}".format(userInput.split(" ", 2)))
            language, activity, dayMonthYear_Hour = userInput.split(" ", 2)
            reply = self.deleteAppointment(activity,
                                           self.datetimeConvert(dayMonthYear_Hour),
                                           address)
            print("DEBUG: {}".format(reply))
        elif userInput.split(" ", 2)[1] == 'almacen':
            language, _, databaseName = userInput.split(" ", 2)
            if Authenticator(self.connection.identifier).is_from_admin(message):
                reply = self.setupDB(databaseName, address)
            else:
                reply = "UR Not allowed 2 do this"
        elif userInput.split(" ", 2)[0] == 'cancelar':
            language, activity, dayMonthYear_Hour = userInput.split(" ", 2)
            reply = self.cancelAppointment(activity, self.datetimeConvert(dayMonthYear_Hour), address)
        elif userInput.split(" ", 2)[0] == 'reservar':
            language, activity, dayMonthYear_Hour = userInput.split(" ", 2)
            reply = self.makeAppointment(activity, self.datetimeConvert(dayMonthYear_Hour), address)
        elif userInput.split(" ")[0] == 'créditos':
            print("Entra pa dar créditos")
            language, credits, activity, address = userInput.split(" ")
            reply = self.giveCredits(address, activity, credits)

        # TODO: Accept double spaces if present...
        # address in WA this is the
        #be telephoneNumber with the @s.whatsapp.net ...

        self.connection.last_used_language = self.appointment[language]
        print("DEBUG: {} is of type {}.\n Language is {}".format(reply,type(reply),self.appointment[language]))
#        self.connection.last_used_timezone = tz
        reply_message = self.generate_reply_message(message, "Appointments...", reply)
        self.send_text_message(reply_message)

    @staticmethod
    def regex_check(message: Message) -> bool:
        """
        Checks if the user input is valid for this service to continue

        :return: True if input is valid, False otherwise
        """
        regex = "^" + Service.regex_string_from_dictionary_keys([AppointmentService.appointment]) \
                + ".*$"
        return re.search(re.compile(regex), message.message_body.lower())
    def makeAppointment(self, activity: str, initHour: datetime, address: str) -> str:
        """
        Will make an appointment for the address at the time for given
        activity.

        :param activity: the name of the activity which is going to be booked 
        :param dayMontYear_Hour: the date tima in any way that parsedatetime
        can understand.
        :param address: the telephone number of the person who sent the message
        :return: information/status message
        """
        # If address is not in appointment database, it will copy it from the bot's database
        print("Is registered user?: {}".format(self.isRegisteredUser(address)))
        # Do your job
#        return ManageAppointments(address, activity,initHour).makeAppointment(address)
        act = db.session.query(Activity).filter_by(name=activity).one()
        allApps = db.session.query(Appointment).filter(Appointment.activity==act).filter(Appointment.initHour>datetime.utcnow())
        apptmnt = db.session.query(Appointment).filter_by(initHour=initHour).filter_by(activity=act).first()
        participant = db.session.query(User).filter_by(wsaddress=address).one()
        print("Vamos a ver si {} tiene un turno en {} ".format(participant.name, apptmnt))
        subs = db.session.query(Appointment).join('enrolled','user').filter(User.wsaddress==participant.wsaddress).filter(Appointment.activity==act).filter(Appointment.initHour==initHour).first()
        """
        Appointment for activity, initHour and user, if exists.
        """
        pulgarBajo = "👎🏽"
        pulgarAlto = "👍🏼"
        if apptmnt is None:
            message = "Ningún turno disponible para *{}* el _{}_\n".format(activity,initHour)
            message += "Hay disponibilidad en:\n"
            for ap in allApps:
                message +="{}\n".format(ap)
        elif subs is None:
            """
            The appointment exists and user has no booked yet
            """
            message = pulgarAlto
            authorized = False
            print(subs)
            print("PrePay: {}".format(act.prePay))
            if act.prePay:
                activityCredits, _ = hasCredit(address, activity)
                if activityCredits is not None:
                    saldo, expireDate = drawCredit(address,activity,1)
                    if saldo >= 0:
                        message = "{}\nCréditos disponibles para {}: {} hasta el {}".format(pulgarAlto,activity,saldo, expireDate)
                        authorized = True
                else:
                     message = "Sin créditos para realizar esta reserva."
                     authorized = False
            if act.prePay is False or authorized:
                try:
                    apptmnt.enrolled.append(MakeAppointment(participant))
                    db.session.add(apptmnt)
                    db.session.commit()
                except:
                    db.session.rollback()

        else:
            message = "Ud. ya tiene reservado un turno para *{}*: {}".format(apptmnt.activity, apptmnt.initHour)
        return message
    def cancelAppointment(self, activity: str, initHour: datetime, address: str) -> str:
        print("Is registered user?: {}".format(self.isRegisteredUser(address)))
        act = db.session.query(Activity).filter_by(name=activity).one()
        apptmnt = db.session.query(Appointment).filter_by(initHour=initHour).filter_by(activity=act).first()
        participant = db.session.query(User).filter_by(wsaddress=address).one()
        print("Vamos a ver si {} tiene un turno en {} el {}".format(participant.name, apptmnt, initHour))
        subs = db.session.query(Appointment).join('enrolled','user').filter(User.name==participant.name).filter(Appointment.initHour==initHour).all()
        print(repr(subs))
        #TODO: Chequear, meparece que le falta la condición de actividadtambién
        return repr(subs) 

    def datetimeConvert(self,dayMonthYear_Hour: str) -> datetime:
        #Will convert human date time to datetime object:
        #TODO: Add locales support.
        c = pdt.Constants(localeID="es", usePyICU=True)
        p = pdt.Calendar(c)
        initHour, tipoFecha = p.parseDT(dayMonthYear_Hour, tzinfo=pytz.timezone(tz))
        print (dayMonthYear_Hour,initHour, tz, pytz.timezone(tz), tipoFecha)
        return initHour


    def createAppointment(self, activity: str, initHour: datetime, address: str, prePay: bool) -> str:
        """
        The bot should ask for a manager after or during
        the activity creation.
        Bla bla bla bla blaaaaa...

        :param activity: the name of the activity to create
        :param dayMontYear_Hour: the datetime in datetime.datetime object.
        :param address: the whatsapp|telegram|email of the person who sent the message
        :return: An confirmation message
        """
        #TODO:Check if the current address has been registered...
        print(self.isRegisteredUser(address))
        #ManageAppointments(address, activity,initHour).createAppointment()
        if Activity.query.filter_by(name=activity).first() is None:
           manager = db.session.query(User).filter_by(wsaddress=address).one()
           act = Activity(activity, manager=manager, prePay=prePay)
           db.session.add(act)
           db.session.commit()
           print(act)
        else:
           print("Entra al else")
           act = db.session.query(Activity).filter_by(name=activity).one()
           print(act)
        appointment = Appointment.query.filter_by(activity=act).filter_by(initHour=initHour)
        if appointment.first() is None:
                appointment = Appointment(act, initHour)
                db.session.add(appointment)
                db.session.commit()
        else:
               appointment = "Ya existe en nuestros registros!: {}".format(appointment.all())
        return repr(appointment)

        # I yet don't konw why, but the EST timezone label apears..., so I'll strip it
#        return "Actividad \"{}\" creada para el {} ...".format(activity,initHour.strftime("%c").rstrip('EST')) #TODO: translate

    def deleteAppointment(self, activity, initHour, address):
        #return ManageAppointments(address, activity=activity, initHour=initHour).deleteInitHour()
        act = db.session.query(Activity).filter_by(name=activity).one()
        print("El ... ... {} y {} ".format(initHour,act))
        apptmnt = db.session.query(Appointment).filter_by(initHour=initHour).filter_by(activity=act).first()
        print(apptmnt)
        message = "Voy a borrar {} ".format(apptmnt)
        db.session.delete(apptmnt)
        try:
            erro = db.session.commit()
        except:
            db.session.rollback()

        if erro is None:
            result = message
        else:
            result = erro
        """
        Some output message
        """
        return result

    def isRegisteredUser(self,address: str) -> str:
        """
        Will check if the sender is not registered as a user.
        """

        addressbook = os.path.join(LocalConfigChecker.contacts_directory, self.connection.identifier, "addressbook.db")
        """
        The addressbook database file path for whatsapp|telegram|mail
        """
        # user = db.session.query(User).filter_by(wsaddress=address).one()
        # The above code gives an  object with all data from that User
#        user = db.session.query(User).filter_by(wsaddress=address).one()
        if User.query.filter_by(wsaddress=address).first() is None: #TODO: avoid only for whatsapp
            try:
                dbk = sqlite3.connect(addressbook)
                cursor = dbk.cursor()
                t = (address,)
                cursor.execute(
                '''SELECT * FROM Contacts WHERE address=?''', t)
                _, name = cursor.fetchone()
                """
                Get the name from kudubot database
                """
                user = User(name,address)
                db.session.add(user)
                db.session.commit()
                """
                Create an User object and save it in flappointment database
                """
            except sqlite3.IntegrityError as e:
                dbk.rollback()
                raise e

            except sqlite3.OperationalError as e:
                dbk.rollback()
                raise e
            except:
                db.session.rollback()
                raise


            return repr(user)
        else:
            return repr(db.session.query(User).filter_by(wsaddress=address).one())

    def giveInfo(self,address: str, date: str = None, offset: str = "7") -> str:
        """
        Will give info about all available activities for today and tomorrow.
        offset: How many days will to "date"
        """
        if date is None:
            onDay = datetime.utcnow()
        else:
            onDay      = self.datetimeConvert(date).replace(hour=0,minute=0)
        untilDay   = onDay + timedelta(int(offset)) # Hardcoded offset
        output = "_*:::Horarios disponibles:::*_\n"
        q = db.session.query(Appointment)
        acts = q.filter(db.and_(Appointment.initHour > onDay, Appointment.initHour < untilDay))
        for row in acts:
            output += "*{}*: {}\n".format(row.activity,row.initHour.strftime("%d %h %H:%M"))
#            output += "*{}*: {}\n".format(row.activity,row.initHour.strftime("%c").rstrip('00').rstrip(':'))
        return output

    def booked(self, address: str) -> str:
        allApps = db.session.query(Appointment).join('enrolled','user').filter(
                 User.wsaddress==address).filter(
                 Appointment.initHour > datetime.utcnow())
        message ="Sus reservas son:\n"
        for ap in allApps:
                message +="{}\n".format(ap)
        return message

    def attended(self, address: str) -> str:
        allApps = db.session.query(Appointment).join('enrolled','user').filter(
                 User.wsaddress==address).filter(
                 Appointment.initHour < datetime.utcnow())
        message ="Asistió a:\n"
        for ap in allApps:
                message +="{}\n".format(ap)
        return message




    def setupDB(self, databaseName: str, address: str) -> str:
        return ManageAppointments(address).setup(databaseName)  #exeption
                                                                #handled inside method

def hasCredit(address: str, activity: str) -> (int,datetime):
    result = None, None
    creds = db.session.query(Credit).join('activity',).join('user').filter(Activity.name==activity).filter(User.wsaddress==address).first()
    if creds is not None:
        result = creds.credits, creds.expireDate
    return result
def drawCredit(address: str, activity: str, credits: int) -> (int,datetime):
    """
    Draw credits and returns saldo and expire date. It does not commit the
    change to database, it relays on the actual appointment process which will
    be done after this action.
    """
    creds =db.session.query(Credit).join('activity',).join('user').filter(Activity.name==activity).filter(User.wsaddress==address).first()
    creds.credits -= credits
    db.session.add(creds)
    #db.session.commit() I believe that the final commit should be done when making the actual appointment, that's why I commented it
    return creds.credits,creds.expireDate

def giveCredits(self, address: str, activity: str, credits: int) -> str:
    usr = User.query.filter_by(wsaddress=address).first()
    if usr is None:
        result = "No hay ningún usuario con ese teléfono"
    else:
        creds = db.session.query(Credit).join('activity',).join('user').filter(
            Activity.name==activity).filter(
            User.wsaddress==usr.wsaddress).first()
        if creds is None:
            act = db.session.query(Activity).filter_by(name=activity).one()
            creds = Credit(usr, act, credits)
            """
            First time credit is given
            """
        else:
           creds.credits += credits
           if creds.expireDate < datetime.utcnow():
               creds.expireDate = datetime.utcnow() + timedelta(days=30)
               """
               30 days after now (if credits already expired)
               """
           else:
               creds.expireDate += timedelta(days=30)
               """
               30 days after the current expire date
               """
        db.session.add(creds)
        db.session.commit()
        result = "Ud. tiene {} créditos con vencimiento el día {}".format(creds.credits, creds.expireDate.strftime("%d %h %Y"))
    return result

