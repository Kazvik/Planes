from texttable.texttable import *
from imports.gameHandlers import GameHandlers

class ConsoleInterface:
    def __init__(self, gameController):
        #function that initializes the ConsoleInterface
        self._game = gameController
        self._columnList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        
    def printShots(self, grid):
        #function that prints a gridShots on the screen
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
        #function that prints a planesGrid on the screen
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
        #function that gets input from the user to place 2 planes.
        print("You need to place 2 planes first.")
        noPlanes = 0
        while noPlanes < 2:
            self.printPlayerGrids()
            cabinCellString = input("Cell of the cabin (e.g. A3): ")
            cabinOrientationString = input("Direction(up/down/left/right): ").lower()
            try:
                self._game.placePlayerPlane(cabinCellString, cabinOrientationString)
                noPlanes += 1
            except ValueError as error:
                print(str(error))

    def printPlayerGrids(self):
        #function that prints the player grids on the screen
        planesGrid = self._game.getPlayerPlanes()
        shotsGrid = self._game.getPlayerShots()
        self.printPlanes(planesGrid)
        self.printShots(shotsGrid)

    def playerHit(self):
        #function that gets input from the user regarding the hit of a cell
        ok = False
        while ok == False:
            cell = input("The cell you want to hit: ")
            ok = True
            hitResult = self._game.PlayerShot(cell)
            print("Player: " + hitResult)

    def PlayerChoice(self):
        #function that calls the PlayerChoice
        self.printPlayerGrids()
        try:
            self.playerHit()
        except Exception as ex:
            print(str(ex))

    def ComputerChoice(self):
        #function that gets the ComputerChoice
        hitResult = self._game.ComputerShot()
        print("Computer: " + hitResult[0])
        
    def runGame(self):
        #function that runs the Game
        self.placePlayerPlanes()
        winner = self._game.getWinner()
        while winner is None:
            self.PlayerChoice()
            winner = self._game.getWinner()
            if winner == "player":
                print("You won! Congratulations!")
                break
            self.ComputerChoice()
            winner = self._game.getWinner()
        if winner == "player":
            print("You won! Congratulations!")
        else:
            print("You lost!")
