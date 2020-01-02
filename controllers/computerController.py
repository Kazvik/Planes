from domain.plane import Plane
from imports.queue import Queue
from imports.gameHandlers import GameHandlers
import random

class ComputerController:
    def __init__(self, computerRepository, planeValidator):
        #function that initializes the ComputerController
        self._computerRepo = computerRepository
        self._planes = []
        self._queue = Queue()
        self._planeValidator = planeValidator
        self.placePlanesRandomly()
      
    def getShots(self):
        #function that gets the ComputerShots
        return self._computerRepo.getShots()

    def getPlanes(self):
        #function that gets the number of the Planes
        return self._computerRepo.getPlanes()

    def addPlane(self, cabinPosition, orientation):
        #function that adds a ComputerPlane
        p = Plane(cabinPosition, orientation)
        self._planeValidator.validate_place(p)
        self._computerRepo.add(p)
        self._planes.append(p)
        
    def placePlanesRandomly(self):
        #function that places 2 planes randomly
        noPlanes = 0
        columns = "ABCDEFGH"
        rows = "12345689"
        directions = ["up", "down", "left", "right"]
        while noPlanes < 2:
            cabinPosition = random.choice(columns) + random.choice(rows)
            orientation = random.choice(directions)
            try:
                self.addPlane(cabinPosition, orientation)
                noPlanes += 1
                print(str(cabinPosition) + str(orientation))
            except Exception as ex:
                pass
                
    def getNoPlanes(self):
        #function that returns the number of ComputerPlanes
        return len(self._planes)

    def checkShot(self, coord):
        #function that checks a Shot based on coordinates ('coord')
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
        #function that marks a missed shot
        self._computerRepo.markBadShot(row, column)

    def markGoodShot(self, row, column):
        #function that marks a successfull shot
        self._computerRepo.markGoodShot(row, column)

    def generateRandomCell(self):
        #function that generates a randomCell
        while True:
            row = random.randint(0, 7)
            column = random.randint(0, 7)
            if self._computerRepo.checkPlaneCell(row, column) == -1:
                return (row, column)

    def NextShot(self):
        #function that determines the NextShot
        if self._queue.size() == 0:
            return self.generateRandomCell()
        else:
            return self._queue.pop()

    @staticmethod
    def bool_cell(row, column):
        #function that returns a row and column
        return row in range(8) and column in range(8)

    def putNeighbors(self, row, column):
        #function that puts the neighbors of a successfull shot in the queue
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for direction in directions:
            if self.bool_cell(row + direction[0], column + direction[1]) == True and self._computerRepo.checkPlaneCell(row + direction[0], column + direction[1]) == -1:
                self._queue.push((row + direction[0], column + direction[1]))
                
