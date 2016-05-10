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

from nose.tools import with_setup
from nose.tools import assert_false
from nose.tools import assert_true

from messengerbot.connection.generic.Message import Message
from messengerbot.services.local_services.XkcdRngService import XkcdRngService


# noinspection PyMethodMayBeStatic
class TestXkcdRngService(object):
    """
    A Unit Test Class for the XKCD RNG Service class
    """

    correct_messages = ["/xkcd-rng", "/xkcd-rng source", "/xkcd-rng quelle"]
    incorrect_messages = ["/xkcd-rng  source", "/xkcd-rng ", "/xkcd-rng quelle  ", "  /xkcd-rng"]
    service = XkcdRngService
    initialized_service = None
    response = ""

    def store_reply(self, reply_message: Message) -> None:
        """
        Stores the reply in a variable

        :param reply_message: the reply
        :return: None
        """
        self.response = reply_message.message_body

    @classmethod
    def setup_class(cls) -> None:
        """
        Sets up the test class

        :return: None
        """
        pass

    @classmethod
    def teardown_class(cls) -> None:
        """
        Tears down the test class

        :return: None
        """
        pass

    def setup(self) -> None:
        """
        Sets up a test

        :return: None
        """

        class Dummy(object):
            """
            Just a dummy connection class
            """
            pass

        dummy_connection = Dummy()
        dummy_connection.last_used_language = "en"
        self.initialized_service = self.service(dummy_connection)
        self.initialized_service.send_text_message = self.store_reply

    def teardown(self) -> None:
        """
        Tears down a test

        :return: None
        """
        pass

    @with_setup(setup, teardown)
    def test_regex(self) -> None:
        """
        Tests the service's regex check

        :return: None
        """
        for message in self.correct_messages:
            message_object = Message(message_body=message, address="")
            print("Testing correct Regex for: " + message)
            assert_true(self.service.regex_check(message_object))
        for message in self.incorrect_messages:
            message_object = Message(message_body=message, address="")
            assert_false(self.service.regex_check(message_object))
            print("Testing incorrect Regex for: " + message)

    def test_response(self) -> None:
        """
        Tests the service's functionality

        :return: None
        """
        message = Message(message_body="/randomkey 100", address="")
        self.initialized_service.process_message(message)
        assert_true(len(self.response) == 100)

    def test_language_switch(self) -> None:
        """
        Tests if the language switch works

        :return: None
        """
        message_en = Message(message_body="/randomkey 1", address="")
        message_de = Message(message_body="/zufallschlüssel 1", address="")
        assert_true(self.initialized_service.connection.last_used_language == "en")
        self.initialized_service.process_message(message_de)
        assert_true(self.initialized_service.connection.last_used_language == "de")
        self.initialized_service.process_message(message_en)
        assert_true(self.initialized_service.connection.last_used_language == "en")
