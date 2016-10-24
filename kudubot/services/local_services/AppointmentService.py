# coding=utf-8
import re
import random
import string
from kudubot.logger.PrintLogger import PrintLogger

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
                    "/turno ": "es",
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
            language, _, activity, dayMonthYear_Hour = message.message_body.lower().split(" ", 2)
            reply = self.createAppointment(activity,
                                           datetimeConvert(dayMonthYear_Hour), address)
        if message.message_body.lower().split(" ", 2)[1] == 'almacen':
            language, _, databaseNamea = message.message_body.lower().split(" ", 2)
            reply = self.setup(activity, datetimeConvert(dayMonthYear_Hour), address)

        else:
            language, activity, dayMonthYear_Hour = message.message_body.lower().split(" ", 2)
            reply = self.addActivity(activity, datetimeConvert(dayMonthYear_Hour), address)
        # TODO: Accept double spaces if present...
        # address in WA this is the
        #be telephoneNumber with the @s.whatsapp.net ...

        self.connection.last_used_language = self.add_activity[language]
#        self.connection.last_used_timezone = tz
        reply_message = self.generate_reply_message(message, "Add Activity", reply)
        self.send_text_message(reply_message)

    @staticmethod
    def regex_check(message: Message) -> bool:
        """
        Checks if the user input is valid for this service to continue

        :return: True if input is valid, False otherwise
        """
        regex = "^" + Service.regex_string_from_dictionary_keys([AddActivity.add_activity]) \
                + ".*$"
        return re.search(re.compile(regex), message.message_body.lower())
    def makeAppointment(self, activity: str, dayMonthYear_Hour: str, address: str) -> str:
        """
        Will make an appointment for the address at the time for given
        activity.

        :param activity: the name of the activity which is going to be booked 
        :param dayMontYear_Hour: the date tima in any way that parsedatetime
        can understand.
        :param address: the telephone number of the person who sent the message
        :return: the random key
        """
        ManageAppointments(address, activity,initHour).makeAppointment()

    def datetimeConvert(self,dayMonthYear_Hour: str) -> datetime.datetime:
        #Will convert human date time to datetime object:
        #TODO: Add locales support.
        c = pdt.Constants(localeID=self.connection.last_used_language, usePyICU=True)
        p = pdt.Calendar(c)
        initHour,_ = p.parseDT(dayMonthYear_Hour, tzinfo=pytz.timezone(tz))
        return initHour


    def addActivity(self, activity: str, dayMonthYear_Hour: str, address: str) -> str:
        """
        Bla bla bla bla blaaaaa...

        :param activity: the name of the activity to create
        :param dayMontYear_Hour: the date tima in any way that parsedatetime
        can understand.
        :param address: the telephone number of the person who sent the message
        :return: the random key
        """
        #TODO: Add locales support.
        c = pdt.Constants(localeID=self.connection.last_used_language, usePyICU=True)
        p = pdt.Calendar(c)
        initHour,_ = p.parseDT(dayMonthYear_Hour, tzinfo=pytz.timezone(tz))
        PrintLogger.print(type(initHour))
        PrintLogger.print(initHour)
        PrintLogger.print(self.connection.last_used_language)
        PrintLogger.print(pytz.timezone(tz))
        ManageAppointments(address, activity,initHour).createAppointment()
#        ap.makeAppointment(activity,initHour):
        # I yet don't konw why, but the EST timezone label apears..., so I'll strip it
	    return "Actividad \"{}\" creada para el {} ...".format(activity,initHour.strftime("%c").rstrip('EST')) #TODO: translate

    def setup(self, databaseName: str, defaultActivity: str,  address: str) -> str:
        if Authenticator(self.connection.identifier).is_from_admin(address):
            try:
                ManageAppointments(address,activity,initHour).setup(databaseName)
                return "Done!"
            except:
                return "Something wen't wrong"
        else:
            return "You are not allowed to do this"


