# -*- coding: utf-8 -*-
import sys
import os
splitPath = sys.argv[0].split("/")
lengthToCut = len(splitPath[len(splitPath) - 1]) + len(splitPath[len(splitPath) - 2]) + 2
upperDirectory = sys.argv[0][:-lengthToCut]
sys.path.append(upperDirectory)

from yowsup.stacks import YowStack
from layer import EchoLayer
from yowsup.layers import YowLayerEvent
from yowsup.layers.auth                        import YowCryptLayer, YowAuthenticationProtocolLayer, AuthError
from yowsup.layers.coder                       import YowCoderLayer
from yowsup.layers.network                     import YowNetworkLayer
from yowsup.layers.protocol_messages           import YowMessagesProtocolLayer
from yowsup.layers.protocol_media              import YowMediaProtocolLayer
from yowsup.layers.stanzaregulator             import YowStanzaRegulator
from yowsup.layers.protocol_receipts           import YowReceiptProtocolLayer
from yowsup.layers.protocol_acks               import YowAckProtocolLayer
from yowsup.layers.logger                      import YowLoggerLayer
from yowsup.layers.protocol_iq                 import YowIqProtocolLayer
from yowsup.layers.protocol_calls              import YowCallsProtocolLayer
from yowsup.common import YowConstants
from yowsup import env
from bot.parsers.configparse import configParse
from bot.parsers.installparser import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--install", help="installs the program", action="store_true")
parser.add_argument("-u", "--update", help="updates the program", action="store_true")
args = parser.parse_args()

installed = isInstalled()

if args.install:
    if installed:
        print("Program already installed. Use --update to update to the newest version")
        sys.exit(1)
    install()
    sys.exit(0)

if not installed:
    print("Program not installed correctly, please use the --install option")
    sys.exit(1)

if args.update:
    update()
    sys.exit(0)

try:
    CREDENTIALS = configParse()
except:
    print("No valid login credentials provided in config file")
    sys.exit(1)

encryptionEnabled = True

if encryptionEnabled:
    from yowsup.layers.axolotl                     import YowAxolotlLayer
    layers = (
        EchoLayer,
        (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer, YowMediaProtocolLayer, YowIqProtocolLayer, YowCallsProtocolLayer),
        YowAxolotlLayer,
        YowLoggerLayer,
        YowCoderLayer,
        YowCryptLayer,
        YowStanzaRegulator,
        YowNetworkLayer
        )
else:
    layers = (
        EchoLayer,
        (YowAuthenticationProtocolLayer, YowMessagesProtocolLayer, YowReceiptProtocolLayer, YowAckProtocolLayer, YowMediaProtocolLayer, YowIqProtocolLayer, YowCallsProtocolLayer),
        YowLoggerLayer,
        YowCoderLayer,
        YowCryptLayer,
        YowStanzaRegulator,
        YowNetworkLayer
    )



stack = YowStack(layers)
stack.setProp(YowAuthenticationProtocolLayer.PROP_CREDENTIALS, CREDENTIALS)         #setting credentials
stack.setProp(YowNetworkLayer.PROP_ENDPOINT, YowConstants.ENDPOINTS[0])    #whatsapp server address
stack.setProp(YowCoderLayer.PROP_DOMAIN, YowConstants.DOMAIN)
stack.setProp(YowCoderLayer.PROP_RESOURCE, env.CURRENT_ENV.getResource())          #info about us as WhatsApp client

stack.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_CONNECT))   #sending the connect signal
# this is the program mainloop
stack.loop()