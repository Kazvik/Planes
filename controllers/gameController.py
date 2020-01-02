from imports.gameHandlers import GameHandlers

class GameController:
    def __init__(self, playerController, computerController):
        #function that initializes the GameController
        self._player = playerController
        self._computer = computerController

    def getPlayerShots(self):
        #function that gets the PlayerShots grid
        return self._player.getShots()

    def getPlayerPlanes(self):
        #function that gets the PlayerPlanes grid
        return self._player.getPlanes()

    def getComputerPlanes(self):
        #function that gets the ComputerPlanes grid
        return self._computer.getPlanes()

    def placePlayerPlane(self, cabinPosition, orientation):
        #function that places a PlayerPlane based on 'cabinPosition' and 'orientation'
        self._player.addPlane(cabinPosition, orientation)

    def getWinner(self):
        #function that gets the winner of the game
        playerPlanesNumber = self._player.getNoPlanes()
        computerPlanesNumber = self._computer.getNoPlanes()
        if computerPlanesNumber == 0:
            return "player"
        if playerPlanesNumber == 0:
            return "computer"
        return None

    def PlayerShot(self, cell):
        #function that makes a PlayerShot based on coordinates 'cell'
        cellPos = GameHandlers.stringToCoordinates(cell)
        r = cellPos[0]
        c = cellPos[1]
        hitResult = self._computer.checkShot(cellPos)
        if hitResult == "You missed!":
            self._player.markBadShot(r, c)
        else:
            self._player.markGoodShot(r, c)
        return hitResult
    
    def ComputerShot(self):
        #function that makes a ComputerShot
        cellPos = self._computer.NextShot()
        r = cellPos[0]
        c = cellPos[1]
        hitResult = self._player.checkShot(cellPos)
        if hitResult == "You missed!":
            self._computer.markBadShot(r, c)
            return hitResult, None
        else:
            self._computer.markGoodShot(r, c)
            if hitResult == "You hit the plane!":
                self._computer.putNeighbors(r, c)
            else:
                self._computer.emptyQueue()
            return hitResult, cellPos
