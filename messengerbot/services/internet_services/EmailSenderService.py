# coding=utf-8
"""
Copyright 2015,2016 Hermann Krumrey

This file is part of messengerbot.

    messengerbot makes use of various third-party python modules to serve
    information via the online chat services.

    messengerbot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    messengerbot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with messengerbot.  If not, see <http://www.gnu.org/licenses/>.
"""

# imports
import re
from typing import Tuple

from messengerbot.servicehandlers.Service import Service
from messengerbot.connection.generic.Message import Message
from messengerbot.connection.email.senders.SmtpSender import SmtpSender
from messengerbot.connection.email.parsers.EmailConfigParser import EmailConfigParser


class EmailSenderService(Service):
    """
    The EmailSenderService Class that extends the generic Service class.
    The service allows the user to send email messages
    """

    identifier = "email_sender"
    """
    The identifier for this service
    """

    help_description = {"en": "/email\tSends an email\n"
                              "syntax: /email <message> [<title>] <recipient>",
                        "de": "/email\tSchickt eine email\n"
                              "syntax: /email <Nachricht> [<titel>] <Empfänger>"}
    """
    Help description for this service.
    """

    no_credentials_message = {"en": "No email credentials stored",
                              "de": "Keine Email Zugangsdaten gespeichert"}
    """
    Message to be shown to the user when no email credentials are stored locally
    """

    email_sent_message = {"en": "Email sent",
                          "de": "Email versandt"}
    """
    Message to be shown when the email was sent.
    """

    def process_message(self, message: Message) -> None:
        """
        Process a message according to the service's functionality

        :param message: the message to process
        :return: None
        """
        email_body, email_title, receiver = self.parse_user_input(message.message_body)
        try:
            credentials = EmailConfigParser.parse_email_config("email")
            reply_message = self.generate_reply_message(message, email_title, email_body)
            reply_message.address = receiver
            SmtpSender(credentials).send_text_email(reply_message)

            reply = self.email_sent_message[self.connection.last_used_language]
            reply_message = self.generate_reply_message(message, "Email Sender", reply)
            self.send_text_message(reply_message)

        except SystemExit:
            reply = self.no_credentials_message[self.connection.last_used_language]
            reply_message = self.generate_reply_message(message, "Email Sender", reply)
            self.send_text_message(reply_message)

    @staticmethod
    def regex_check(message: Message) -> bool:
        """
        Checks if the user input is valid for this service to continue

        :return: True if input is valid, False otherwise
        """
        return re.search(r"^/email (\"[^\"]+\") (\"[^\"]+\" )?[^ ]+@[^ ]+$", message.message_body)

    @staticmethod
    def parse_user_input(user_input) -> Tuple[str, str, str]:
        """
        Parses the user input and determines the message bod + title to send and also the receiver of the email

        :param user_input: the input to be checked
        :return: a tuple of message body, message title and receiving email address
        """

        parts = user_input.split("/email ")[1]

        body = parts.split("\"", 2)[1]
        parts = parts.split("\"", 2)[2]

        if re.search(r" (\"[^\"]+\" )[^ ]+@[^ ]+$", parts):
            title = parts.split("\"", 2)[1]
        else:
            title = ""

        receiver = parts.rsplit(" ")[1]

        return body, title, receiver