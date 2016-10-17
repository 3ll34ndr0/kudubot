# coding=utf-8
import re
import random
import string

from kudubot.servicehandlers.Service import Service
from kudubot.connection.generic.Message import Message
import sys
sys.path.append('/home/lean/arena/10cur4')
from manager import ManageAppointments

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
			      "/addactivity actividad dd/mm/aa hh:mm",
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
        language, length = message.message_body.lower().split(" ", 1)
        self.connection.last_used_language = self.add_activity[language]

        reply = self.addActivity(int(length))
        reply_message = self.generate_reply_message(message, "Add Activity", reply)
        self.send_text_message(reply_message)

    @staticmethod
    def regex_check(message: Message) -> bool:
        """
        Checks if the user input is valid for this service to continue

        :return: True if input is valid, False otherwise
        """
        regex = "^" + Service.regex_string_from_dictionary_keys([AddActivity.add_activity]) \
                + " [1-9]{1}[0-9]*$"
        return re.search(re.compile(regex), message.message_body.lower())

    def addActivity(self, length: int) -> str:
        """
        Generates a random key of specified length using the alphabet specified as class variable

        :param length: the length of the keyphrase
        :return: the random key
        """
        random_key = ""
        if length > 100:
            return "Sorry"
        for x in range(0, length):
            random_key += random.choice(self.alphabet)
        return random_key
