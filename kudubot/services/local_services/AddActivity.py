# coding=utf-8
import re
import random
import string
from kudubot.logger.PrintLogger import PrintLogger

from kudubot.servicehandlers.Service import Service
from kudubot.connection.generic.Message import Message
import sys
sys.path.append('/home/lean/arena/10cur4')
import parsedatetime as pdt
import pytz
from datetime import datetime

from manager import ManageAppointments
tz = "America/Argentina/Cordoba" #TODO: Avoid hardcoded values
class AddActivity(Service):
    """
    The RandomKeyGeneratorService Class that extends the generic Service class.
    The service sends a random key of specified length
    """

    identifier = "add_activity"
    """
    The identifier for this service
    """

    help_description = {"en": "/addactivity\t creates a new activity\n"
                              "syntax:\n"
                              "/addactivity activity_name DD/MM/AAAA hh:mm",
                        "es": "/agregaractividad\tCrea una nueva actividad\n"
                              "uso (por ejemplo):\n"
                              "/agregaractividad nombreActividad 24/10/16 12:30"}
    """
    Help description for this service.
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    """
    The alphabet to be used to generate a random key
    """


    add_activity = {"/addactivity": "en",
                    "/agregaractividad": "es"}
    """
    Keywords for the /randomkey command
    """

    def process_message(self, message: Message) -> None:
        """
        Process a message according to the service's functionality

        :param message: the message to process
        :return: None
        """
        language, activity, dayMonthYear_Hour = message.message_body.lower().split(" ", 2)
        # TODO: Accept double spaces if present...
        address, _ = message.get_individual_address().split("@",1) #For WA
        # address in WA this is the
        # telephoneNumber with the @s.whatsapp.net ...

        self.connection.last_used_language = self.add_activity[language]
        self.connection.last_used_timezone = tz
        reply = self.addActivity(activity, dayMonthYear_Hour, address)
#        reply = activity
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

    def addActivity(self, activity: str, dayMonthYear_Hour: str, address: str) -> str:
        """
        Generates a random key of specified length using the alphabet specified as class variable

        :param length: the length of the keyphrase
        :return: the random key
        """
        #TODO: Add locales support.
        c = pdt.Constants(localeID=self.connection.last_used_language, usePyICU=False)
        p = pdt.Calendar(c)
        initHour,_ = p.parseDT(dayMonthYear_Hour, tzinfo=pytz.timezone(self.connection.last_used_timezone))
        PrintLogger.print(type(initHour))
        PrintLogger.print(dir(initHour))
        ap = ManageAppointments(address, activity,initHour)
#        ap.makeAppointment(activity,initHour):

        return "Actividad creada..." 
