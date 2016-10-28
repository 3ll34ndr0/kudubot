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
import parsedatetime as pdt
import pytz
import datetime
tz = "America/Argentina/Cordoba" #TODO: Avoid hardcoded values
from pytz import country_timezones
# Guardo aca algunos métodos de pytz pa no olvidarme.
# country_timezones('ar') tira una lista de los horarios de cada pais, en este caso Argentina.
#horarioCordoba = pytz.timezone('America/Argentina/Cordoba')
#horarioCordoba.zone

from manager import ManageAppointments

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

    appointment = {"/appointment": "en",
                    "/turno": "es",
                    "/reservar": "es"}
    """
    Keywords for the /appointment command
    """

    def process_message(self, message: Message) -> None:
        """
        Process a message according to the service's functionality

        :param message: the message to process
        :return: None
        """
        if self.connection.identifier == 'whatsapp':
            address, _ = message.get_individual_address().split("@",1) #For WA

        if message.message_body.lower().split(" ", 2)[1] == 'nuevo':
            language, _, activity, dayMonthYear_Hour = message.message_body.lower().split(" ", 3)
            PrintLogger.print(type(dayMonthYear_Hour))
            reply = self.createAppointment(activity,
                                           self.datetimeConvert(dayMonthYear_Hour), address)
        elif message.message_body.lower().split(" ", 2)[1] == 'almacen':
            language, _, databaseName = message.message_body.lower().split(" ", 2)
            if Authenticator(self.connection.identifier).is_from_admin(message):
                reply = self.setupDB(databaseName, address)
            else:
                reply = "UR Not allowed 2 do this"
        else:
            language, activity, dayMonthYear_Hour = message.message_body.lower().split(" ", 2)
            reply = self.makeAppointment(activity, self.datetimeConvert(dayMonthYear_Hour), address)
        # TODO: Accept double spaces if present...
        # address in WA this is the
        #be telephoneNumber with the @s.whatsapp.net ...

        self.connection.last_used_language = self.appointment[language]
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
    def makeAppointment(self, activity: str, initHour: datetime.datetime, address: str) -> str:
        """
        Will make an appointment for the address at the time for given
        activity.

        :param activity: the name of the activity which is going to be booked 
        :param dayMontYear_Hour: the date tima in any way that parsedatetime
        can understand.
        :param address: the telephone number of the person who sent the message
        :return: the random key
        """
        return ManageAppointments(address, activity,initHour).makeAppointment(address,activity,initHour)

    def datetimeConvert(self,dayMonthYear_Hour: str) -> datetime.datetime:
        #Will convert human date time to datetime object:
        #TODO: Add locales support.
        c = pdt.Constants(localeID=self.connection.last_used_language, usePyICU=True)
        p = pdt.Calendar(c)
        initHour,_ = p.parseDT(dayMonthYear_Hour, tzinfo=pytz.timezone(tz))
        return initHour


    def createAppointment(self, activity: str, initHour: datetime.datetime, address: str) -> str:
        """
        Bla bla bla bla blaaaaa...

        :param activity: the name of the activity to create
        :param dayMontYear_Hour: the date tima in any way that parsedatetime
        can understand.
        :param address: the telephone number of the person who sent the message
        :return: the random key
        """
	#TODO:Check if the current address has been registered...

	if address is not in addressbook:
		createUserRegisterDB(database=None,phone=None,name=None, activity=None, credit=None, vCard=None, expDate=None)
	#
        ManageAppointments(address, activity,initHour).createAppointment()
        # I yet don't konw why, but the EST timezone label apears..., so I'll strip it
        return "Actividad \"{}\" creada para el {} ...".format(activity,initHour.strftime("%c").rstrip('EST')) #TODO: translate


        def isRegisteredUser(self,address):
        """
        Will check if the sender is not registered as a user.
        """

        addressbook = os.path.join(LocalConfigChecker.contacts_directory, "whatsapp", "addressbook.db")
        """
        The addressbook database file path
        """
	if ManageAppointments(address).getUserRegister() is None:
        try:
            db = sqlite3.connect(addressbook)
            cursor = db.cursor()
            t = (address+'@s.whatsapp.net',)
            cursor.execute(
            '''SELECT * FROM Contacts WHERE adress=?''', t)
            phone, name = cursor.fetchone()
            if phone is None:
                return "Error: Number not found..."
            else:
                ManageAppointments(address,
                                   activity,initHour).createUserRegisterDB()

    except sqlite3.IntegrityError as e:
        db.rollback()
        raise e
    except sqlite3.OperationalError as e:
        db.rollback()
        raise e
    finally:
        cursor.close()



    def setupDB(self, databaseName: str, address: str) -> str:
        return ManageAppointments(address).setup(databaseName)  #exeption
                                                                #handled inside method


