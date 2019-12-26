from texttable.texttable import *
from imports.gameHandlers import GameHandlers

class ConsoleInterface:
    def __init__(self, gameController):
        self._game = gameController
        self._columnList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        
    def printShots(self, grid):
        textTable = Texttable()
        textTable.add_row([' '] + self._columnList)
        for i in range(8):
            row = [str(i + 1)]
            for j in range(8):
                entry = ' '
                if grid[i][j] == 0:
                    entry = '-'
                elif grid[i][j] == 1:
                    entry = '+'
                row += [entry]
            textTable.add_row(row)
        print("______________SHOTS GRID______________")
        print(textTable.draw())
        print("______________SHOTS GRID______________")

    def printPlanes(self, grid):
        textTable = Texttable()
        textTable.add_row([' '] + self._columnList)
        for i in range(8):
            row = [str(i + 1)]
            for j in range(8):
                entry = ' '
                if grid[i][j] == 1:
                    entry = 'P'
                if grid[i][j] == 0:
                    entry = 'X'
                row += [entry]
            textTable.add_row(row)
        print("______________PLANES GRID______________")
        print(textTable.draw())
        print("______________PLANES GRID______________")

    def placePlayerPlanes(self):
        print("Place 2 planes first.")
        noPlanes = 0
        while noPlanes < 2:
            self.printPlayerGrids()
            cabinCellString = input("Please provide the cell of the cabin (e.g. A3, C7, H5 etc.): ")
            cabinOrientationString = input("Please provide where the cabin should point to (up/down/left/right): ").lower()
            try:
                self._game.placePlayerPlane(cabinCellString, cabinOrientationString)
                noPlanes += 1
            except ValueError as error:
                print(str(error))

    def printPlayerGrids(self):
        planesGrid = self._game.getPlayerPlanes()
        shotsGrid = self._game.getPlayerShots()
        self.printPlanes(planesGrid)
        self.printShots(shotsGrid)

    def playerHit(self):
        ok = False
        while ok == False:
            cell = input("Enter the cell you want to hit (e.g. A1): ")
            ok = True
            hitResult = self._game.PlayerShot(cell)
            print(hitResult)

    def PlayerChoice(self):
        options = {
            "1" : self.playerHit,
            "2" : self.printPlayerGrids
        }
        ok = 0
        while ok != 1:
            print("1.Enter a cell to hit.")
            print("2.View the grids.")
            option = input("Option: ")
            try:
                if option not in options:
                    raise Exception("Enter a valid option.")
                options[option]()
                ok = 1 
            except Exception as e:
                print(str(e))

    def ComputerChoice(self):
        hitResult = self._game.ComputerShot()
        print(hitResult[0])
        
    def runGame(self):
        self.placePlayerPlanes()
        winner = self._game.getWinner()
        while winner is not None:
            self.PlayerChoice()
            self.ComputerChoice()
            winner = self._game.getWinner()
        if winner == "player":
            print("You won! Congratulations!")
        else:
            print("You lost!")
