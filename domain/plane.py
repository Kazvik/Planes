from imports.gameHandlers import GameHandlers

class Plane():
    #the plane class which represents a plane object
    
    def __init__(self, cabinPosition, orientation):
        #cabinPosition = str, a combination of a letter (A -> H) and a digit (1-> 8)
        #orientation = str, it could be one of the following ('up', 'down', 'left', 'right')
        self._pos = cabinPosition
        self._orientation = orientation
        
    def getPos(self):
        #returns the cabinPosition of a plane
        return self._pos
    
    def getOrientation(self):
        #returns the orientation of a plane
        return self._orientation
    
    def getPlaneCells(self):
        #returns a list with all the cells of a plane
        directions = GameHandlers.getDirections(self._orientation)
        sign = GameHandlers.getSign(self._orientation)
        cells = []   
        position = GameHandlers.stringToCoordinates(self._pos)
        for d in directions:
            #row
            r = position[0] + sign * d[0]
            #column
            c = position[1] + sign * d[1]
            cells.append((r, c))
        return cells