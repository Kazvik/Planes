from imports.gameHandlers import GameHandlers

class GameController:
    def __init__(self, playerController, computerController):
        self._player = playerController
        self._computer = computerController

    def getPlayerShots(self):
        return self._player.getShots()

    def getPlayerPlanes(self):
        return self._player.getPlanes()

    def getComputerPlanes(self):
        return self._computer.getPlanes()

    def placePlayerPlane(self, cabinPosition, orientation):
        self._player.addPlane(cabinPosition, orientation)

    def getWinner(self):
        playerPlanesNumber = self._player.getNoPlanes()
        computerPlanesNumber = self._computer.getNoPlanes()
        if computerPlanesNumber == 0:
            return "player"
        if playerPlanesNumber == 0:
            return "computer"
        return None

    def PlayerShot(self, cell):
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
