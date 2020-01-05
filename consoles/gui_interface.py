from tkinter import *
from imports.gameHandlers import GameHandlers

class GuiInterface():
    
    def __init__(self, gameController):
        #function that initializes the GuiInterface
        self._game = gameController
        self._columnList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

        #Tkinter
        