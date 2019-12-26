

class GameHandlers():
    
    def __init__(self):
        pass
    
    @staticmethod
    def getDirections(direction):
        #function that returns the list of a direction
        #direction - str
        updown = [(0, 0), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, 0), (3, -1), (3, 0), (3, 1)]
        leftright = [(0, 0), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (0, 2), (-1, 3), (0, 3), (1, 3)]
        directions = {
            "up" : updown,
            "down" : updown,
            "left" : leftright,
            "right" : leftright
        }
        return directions[direction]
    
    @staticmethod
    def getSign(direction):
        #function that returns the sign of a direction
        #direction - str
        directions = {
            "up" : 1,
            "down" : -1,
            "left" : 1,
            "right" : -1
        }
        return directions[direction]
    
    @staticmethod
    def stringToCoordinates(position):
        realColumn = {
            'A': 0, 
            'B': 1, 
            'C': 2, 
            'D': 3, 
            'E': 4, 
            'F': 5, 
            'G': 6, 
            'H': 7
        }
        realRow = {
            '1': 0, 
            '2': 1, 
            '3': 2, 
            '4': 3, 
            '5': 4, 
            '6': 5, 
            '7': 6, 
            '8': 7
        }
        return (realRow[position[1]], realColumn[position[0]])
        