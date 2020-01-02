from domain.plane import Plane
from imports.gameHandlers import GameHandlers


class PlayerController():
    
    def __init__(self, playerRepository, planeValidator):
        #function that initializes the PlayerController
        self._playerRepo = playerRepository
        self._planes = []
        self._planeValidator = planeValidator

    def getShots(self):
        #function that returns the shots grid of the player
        return self._playerRepo.shotsGrid()
    
    def getPlanes(self):
        #function that returns the planes grid of the player
        return self._playerRepo.planesGrid()
    
    def addPlane(self, cabinPosition, orientation):
        #function that adds a new plane based on 'cabinPosition' and 'orientation'
        p = Plane(cabinPosition, orientation)
        self._planeValidator.validate_place(p)
        self._playerRepo.add(p)
        self._planes.append(p)
    
    def getNoPlanes(self):
        #function that returns the number of planes
        return len(self._planes)
    
    def markGoodShot(self, r, c):
        #function that marks a successfull shot
        self._playerRepo.markGoodShot(r,c)
    
    def markBadShot(self, r, c):
        #function that marks a missed shot
        self._playerRepo.markBadShot(r,c)
    
    def checkShot(self, coord):
        #function that checks a shot based on coordinates ('coord')
        response = ""
        r = coord[0]
        c = coord[1]
        value = self._playerRepo.checkPlaneCell(r, c)
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
            self._playerRepo.hit(r, c)
        else:
            response = "You missed!"
        return response
        