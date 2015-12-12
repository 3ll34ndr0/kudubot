"""
A GUI for the Plugin Manager
@author Hermann Krumrey<hermann@krumreyh.com>
"""

from tkinter import *

"""
The PluginManagerGUI class
"""
class PluginManagerGUI(object):

    """
    Constructor that starts the GUI
    """
    def __init__(self, pluginManager):

        self.pluginManager = pluginManager
        self.gui = Tk()

        self.buttons = {}

        for key in self.pluginManager.plugins:
            button = Button(self.gui, text=key, background="green", command=lambda key=key:self.__toggleValue__(key))
            self.buttons[key] = button
            button.pack()

        Button(self.gui, text="Confirm", command=self.gui.destroy).pack()

        self.gui.mainloop()

    """
    Toggles the value of a button
    """
    def __toggleValue__(self, key):

        if self.pluginManager.plugins[key]:
            self.pluginManager.plugins[key] = False
            self.buttons[key].config(background='red')
        else:
            self.pluginManager.plugins[key] = True
            self.buttons[key].config(background='green')