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

import re
import os
import time
import datetime
import configparser
from yowsup.layers.protocol_messages.protocolentities import TextMessageProtocolEntity
from plugins.GenericPlugin import GenericPlugin

"""
The Casino Class
"""
class Casino(GenericPlugin):

    casinoDir = os.getenv("HOME") + "/.whatsapp-bot/casino/"
    userDir = casinoDir + "users/"

    """
    Constructor
    Defines parameters for the plugin.
    @:param layer - the overlying yowsup layer
    @:param messageProtocolEntity - the received message information
    @:override
    """
    def __init__(self, layer, messageProtocolEntity=None):
        if messageProtocolEntity is None: self.layer = layer; return
        self.layer = layer
        self.entity = messageProtocolEntity
        self.message = self.entity.getBody().lower()
        self.sender = self.entity.getFrom()
        self.user = self.entity.getParticipant()
        if not self.user: self.user = self.entity.getFrom()
        self.userID = self.user.split("@")[0]
        self.userNick = self.entity.getNotify()
        self.reply = None

    """
    Checks if the user input is valid for this plugin to continue
    @:return True if input is valid, False otherwise
    @:override
    """
    def regexCheck(self):
        return re.search(r"^/casino (balance|beg)$", self.message)

    """
    Parses the user's input
    @:override
    """
    def parseUserInput(self):
        self.createUser(self.entity)
        mode = self.message.split("/casino ")[1]

        replyText = ""
        if mode == "balance":
            balance = self.getBalance(self.userID)
            replyText = "Your balance is: " + self.encodeMoneyString(balance[0], balance[1], True) + "€"
        elif mode == "beg":
            self.transferFunds(self.userID, 1, 0)
            replyText = "You earn 1€ while begging for money"

        self.reply = TextMessageProtocolEntity(replyText, to=self.sender)

    """
    Returns the response calculated by the plugin
    @:return the response as a MessageProtocolEntity
    @:override
    """
    def getResponse(self):
        return self.reply

    """
    Returns a helpful description of the plugin's syntax and functionality
    @:param language - the language to be returned
    @:return the description as string
    @:override
    """
    @staticmethod
    def getDescription(language):
        if language == "en":
            return "/casino\tprovides basic casino functions\n" \
                   "syntax:\n" \
                   "/casino balance\tsends you your current balance"
        elif language == "de":
            return "/casino\tBietet simple Casino Funktionen\n" \
                   "syntax:\n" \
                   "/casino balance\tSchickt den momentanen Kontostand des Nutzers"
        else:
            return "Help not available in this language"

    """
    Starts a parallel background activity if this class has one.
    Defaults to False if not implemented
    @:return False, if no parallel activity defined, should be implemented to return True if one is implmented.
    @:override
    """
    def parallelRun(self):
        while True:
            currentTime = datetime.datetime.now()
            hours = int(currentTime.hour)
            if not hours < 23:
                for user in os.listdir(self.userDir):
                    self.transferFunds(user, 2000, 0)
            time.sleep(3600)


    """
    Creates a new user file
    @:param messageEntity - a messageEntity sent from the user
    """
    def createUser(self, messageEntity):
        userID = messageEntity.getParticipant()
        if not userID: userID = messageEntity.getFrom(False)
        userID = userID.split("@")[0]
        userNick = messageEntity.getNotify()
        userFile = self.userDir + userID

        if not os.path.isfile(userFile):
            self.generateUser(userID, userNick, "1000.00")

    """
    Generates a user account
    @:param userID - the user's ID
    @:param userNick - the user's (nick)name
    @:param balance - the user's balance
    """
    def generateUser(self, userID, userNick, balance):
        userFile = self.userDir + userID
        file = open(userFile, "w")
        file.write("[account]\n")
        file.write("nick=" + userNick + "\n")
        file.write("balance=" + balance)

    """
    Gets the user's (nick)name from his/her account
    @:param userId - the user's ID
    @:return the user's (nick)name
    """
    def getUserNick(self, userId):
        userFile = self.userDir + userId
        userDetails = configparser.ConfigParser()
        userDetails.read(userFile)
        nick = dict(userDetails.items("account"))["nick"]
        return nick


    """
    Gets the balance of a user
    @:param userID - the user's ID
    @:return the user's balance
    """
    def getBalance(self, userID):
        userFile = self.userDir + userID
        userDetails = configparser.ConfigParser()
        userDetails.read(userFile)
        balance = dict(userDetails.items("account"))["balance"]
        return self.decodeMoneyString(balance)

    """
    Sets a user's balance to a specified value
    @:param userID - the user's ID
    @:param dollars - the amount of dollars
    @:param cents - the amount of cents
    """
    def setBalance(self, userID, dollars, cents):
        balanceString = self.encodeMoneyString(dollars, cents)
        userNick = self.getUserNick(userID)
        self.generateUser(userID, userNick, balanceString)

    """
    Decodes a money string
    @:param moneyString - the String to be decoded
    @:return the monetary value as a tuple of dollars and cents
    """
    def decodeMoneyString(self, moneyString):
        dollars = int(moneyString.split(".")[0])
        try:
            cents = moneyString.split(".")[1]
            if len(cents) < 2: cents += "0"
            cents = int(cents)
        except:
            cents = 0
        return (dollars, cents)

    """
    Encodes a tuple of dollars and cents to a moneyString
    @:param dollars - the amount of dollars
    @:param cents - the amount of cents
    @:param delimiters - switch for enabling delimiters
    @:return the encoded dollar string
    """
    def encodeMoneyString(self, dollars, cents, delimiters=False):
        centString = str(cents)
        if len(centString) < 2: centString = "0" + centString
        if len(centString) < 2: centString = "0" + centString
        if not delimiters:
            return str(dollars) + "." + centString
        else:
            dollarString = str(dollars)
            dollarList = []
            for char in dollarString: dollarList.insert(0, char)
            print(dollarList)
            formatedDollarString = ""
            i = 0
            while i < len(dollarList):
                if i > 0 and i % 3 == 0:
                    formatedDollarString = " " + formatedDollarString
                formatedDollarString = dollarList[i] + formatedDollarString
                i += 1
            return formatedDollarString + "." + centString

    """
    Multiplies a monetary value by a given factor
    @:param factor - the actor with which to multiply
    @:param dollars - the initial amount of dollars
    @:param cents - the initial amount of cents
    @:return the multiplied monetary value as a tuple of dollars and cents
    """
    def multiplyMoney(self, factor, dollars, cents):
        multipliedDollars = factor * dollars
        multipliedCents = factor * cents
        while multipliedCents >= 100: multipliedCents -= 100; multipliedDollars += 1
        return (multipliedDollars, multipliedCents)


    """
    Adds or subtracts an amount from the balance of a player
    @:param userID - the user's ID
    @:param dollars - the amount of dollars to be transferred
    @:param cents - the amount of cents to be transferred
    """
    def transferFunds(self, userID, dollars, cents):
        currentDollars, currentCents = self.getBalance(userID)
        newCents = currentCents + cents
        while newCents >= 100: currentDollars += 1; newCents -= 100
        while newCents < 0: currentDollars -= 1; newCents += 100
        newDollars = currentDollars + dollars
        self.setBalance(userID, newDollars, newCents)

    """
    Checks if a user has enough funds for a specified bet
    @:param userID - the user's ID
    @:param dollars - the amount of dollars to be bet
    @:param cents - the amount of cents to be bet
    @:return True if the user has enough funds, False otherwise
    """
    def hasSufficientFunds(self, userID, dollars, cents):
        currentDollars, currentCents = self.getBalance(userID)
        currentMoney = (currentDollars * 100) + currentCents
        queryValue = (dollars * 100) + cents
        return queryValue <= currentMoney

    """
    Stores a bet to a user's bet file
    @:param game - the game played
    @:param userID - the user's ID
    @:param sender - the sender of the bet
    @:param dollars - the bet mount (dollars)
    @:param cents - the bet amount (cents)
    @:param betType - the bet type identifier
    """
    def storeBet(self, game, userID, sender, dollars, cents, betType):
        betString = sender + ";" + self.encodeMoneyString(dollars, cents) + ";" + betType + "\n"
        userBets = open(self.casinoDir + game + "/" + userID, "a")
        userBets.write(betString)
        userBets.close()

    """
    Gets the bets from a user's bet file
    @:param game - the game played
    @:param userID - the user's ID
    @:return the bets as a list of strings
    """
    def getBets(self, game, userID):
        betFile = open(self.casinoDir + game + "/" + userID, "r")
        rawBets = betFile.read().split("\n")
        rawBets.pop()
        betFile.close()
        bets = []

        for bet in rawBets:
            betParts = bet.split(";")
            betDict = {"sender" : betParts[0], "value" : betParts[1], "bet" : betParts[2]}
            bets.append(betDict)

        return bets

    """
    Gets the bets of a user as strings
    @:param game - the game played
    @:param userID - the user's ID
    return the bets as a string
    """
    def getBetStrings(self, game, userID):
        betString = "You have bet on the following:"
        try:
            bets = self.getBets(game, userID)
            for bet in bets:
                dollars, cents = self.decodeMoneyString(bet["value"])
                betVal = self.encodeMoneyString(dollars, cents, True)
                betString += "\nBet: " + bet["bet"] + "     Amount: " + betVal + "€"
        except:
            print()
        return betString