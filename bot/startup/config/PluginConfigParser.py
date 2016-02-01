# coding=utf-8
"""
Copyright 2015,2016 Hermann Krumrey

This file is part of whatsapp-bot.

    whatsapp-bot makes use of various third-party python modules to serve
    information via the online chat service Whatsapp.

    whatsapp-bot is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    whatsapp-bot is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with whatsapp-bot.  If not, see <http://www.gnu.org/licenses/>.
"""

import os

"""
The PluginConfigParser Class
"""
class PluginConfigParser(object):

    """
    Constructor
    """
    def __init__(self):
        self.configFile = os.getenv("HOME") + "/.whatsapp-bot/plugins"

    def readPlugins(self):
        pluginDictionary = {}
        file = open(self.configFile, 'r')
        for line in file:
            pluginName = line.rsplit("=", 1)[0]
            pluginState = line.rsplit("=", 1)[1]
            if "1" in pluginState:
                pluginDictionary[pluginName] = True
            else:
                pluginDictionary[pluginName] = False
        file.close()
        return pluginDictionary

    def writePlugins(self, pluginDictionary):
        file = open(self.configFile, "w")
        for name in pluginDictionary:
            state = "0"
            if pluginDictionary[name]: state = "1"
            file.write(name + "=" + state + "\n")
        file.close()