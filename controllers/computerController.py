from domain.plane import Plane
from imports.queue import Queue
from imports.gameHandlers import GameHandlers
import random

class ComputerController:
    def __init__(self, computerRepository, planeValidator):
        self._computerRepo = computerRepository
        self._planes = []
        self._queue = Queue()
        self._planeValidator = planeValidator
        #self.placePlanesRandomly()
        
    def getShots(self):
        return self._computerRepo.getShots()

    def getPlanes(self):
        return self._computerRepo.getPlanes()

    def addPlane(self, cabinPosition, orientation):
        p = Plane(cabinPosition, orientation)
        self._planeValidator.validateplane(p)
        self._computerRepo.add(p)
        self._planes.append(p)
        
    def placePlanesRandomly(self):
        noPlanes = 0
        columns = "ABCDEFGH"
        rows = "12345689"
        directions = ["up", "down", "left", "right"]
        while noPlanes < 2:
            cabinPosition = random.choice(columns) + random.choice(rows)
            orientation = random.choice(directions)
            try:
                self.placePlane(cabinLocation, cabinOrientation)
                noPlanes += 1
            except:
                pass

    def getNoPlanes(self):
        return len(self._planes)

    def checkShot(self, coord):
        r = coord[0]
        c = coord[1]
        value = self._computerRepo.checkPlaneCell(r, c)
        if value != -1:
            if value == 1:
                response = "You hit the plane!"
                i = 0
                while i < len(self._planes):
                    p = self._planes[i]
                    if coord == GameHandlers.stringToCoordinates(p.getPos()):
                        value = 0
                        response = "You hit the Cabin!"
                        del self._planes[i]
                        break
                    i = i + 1
            self._computerRepo.hit(r, c)
        else:
            response = "You missed!"
        return response
    
    def markBadShot(self, row, column):
        self._computerRepo.markBadShot(row, column)

    def markGoodShot(self, row, column):
        self._computerRepo.markGoodShot(row, column)

    def generateRandomCell(self):
        while True:
            row = random.randint(0, 7)
            column = random.randint(0, 7)
            if self._computerRepo.checkPlaneCell(row, column) == -1:
                return (row, column)

    def NextShot(self):
        if self._queue.size() == 0:
            return self.generateRandomCell()
        else:
            return self._queue.pop()

    @staticmethod
    def bool_cell(row, column):
        return row in range(8) and column in range(8)

    def putNeighbors(self, row, column):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            if self.bool_cell(row + direction[0], column + direction[1]) == True and self._computerRepo.checkPlaneCell(row + direction[0], column + direction[1]) == -1:
                self._queue.push((row + direction[0], column + direction[1]))

    def emptyQueue(self):
        self._queue.clear()

