# coding=utf-8
"""
LICENSE:
Copyright 2015,2016 Hermann Krumrey

This file is part of kudubot.

    kudubot makes use of various third-party python modules to serve
    information via online chat services.

    kudubot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    kudubot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with kudubot.  If not, see <http://www.gnu.org/licenses/>.
LICENSE
"""

# imports
import re

from kudubot.servicehandlers.Service import Service
from kudubot.connection.generic.Message import Message
from kudubot.resources.terminal.Data import destinos
from kudubot.logger.PrintLogger import PrintLogger


class TerminalService(Service):
    """
    The KvvService Class that extends the generic Service class.
    The service checks the curent timetables from the KVV Straßenbahn Network
    and displays the most relevant times
    """

    identifier = "horarios"
    """
    The identifier for this service
    """

    help_description = {"en": "/departures\tShows timetable information for Concordia\n"
                              "syntax:\n"
                              "/kvv <station>",
                        "es": "horarios\tMuestra horarios de partida a una localidad desde Concordia\n"
                              "uso:\n"
                              "horarios Ciudad_destino"}
    """
    Help description for this service.
    """


    corrections = {"hauptbahnhof": "karlsruhe hauptbahnhof",
                   "vorplatz": "karlsruhe hbf vorplatz",
                   "karlruhe hauptbahnhof vorplatz": "karlsruhe hbf vorplatz",
                   "hauptbahnhof vorplatz": "karlsruhe hbf vorplatz"}
    """
    Corrections for the station parameter given by the user to attempt to deliver more relevant
    search results
    """

    def process_message(self, message: Message) -> None:
        """
        Process a message according to the service's functionality

        :param message: the message to process
        :return: None
        """
        mensage = message.message_body.split(" ",1)
        PrintLogger.print(mensage)
        if len(mensage) == 1: 
            destino = None
        else:
            destino = message.message_body.split(" ", 1)[1].lower()
        if destino == None or destino == 'destinos':
            reply = self.getDestinos()
        else:
            reply = self.getDestinoInfo(destino)
        reply_message = self.generate_reply_message(message, "Horarios Terminal Concordia", reply)
        self.send_text_message(reply_message)

    @staticmethod
    def regex_check(message: Message) -> bool:
        """
        Checks if the user input is valid for this service to continue

        :return: True if input is valid, False otherwise
        """
        regex = "^horarios"
        return re.search(re.compile(regex), message.message_body.lower())

    def getDestinos(self) -> str:
        return 'Destinos disponibles: {}'.format(' '.join(list(destinos.keys())))

    def getDestinoInfo(self, city: str) -> str:
        """
        Gets information for a selected city 

        :param city: the city for which information should be looked up
        :return: the information for that city departures 
        """

        return destinos[city]


