

class PlaneValidator():
    
    def __init__(self):
        pass
    
    @staticmethod
    def validate_letter(letter):
        #function that validates if a letter is between A and H
        #letter - str
        if letter < 'A' or letter > 'H':
            raise ValueError("Letter must be one of the following: A, B, C, D, E, F, G, H!")
    
    @staticmethod
    def validate_digit(digit):
        #function that validates if a digit is between 1 and 8
        #digit - str
        if int(digit) < 1 or int(digit) > 8:
            raise ValueError("Digit must be one of the following: 1, 2, 3, 4, 5, 6, 7, 8!")
    
    def validate_coordinate(self, string_coordinate):
        #function that validates if a given coordinate is valid
        self.validate_letter(string_coordinate[0])
        self.validate_digit(string_coordinate[1])
    
    def validate_place(self, plane):
        #function that validates if a plane can be placed in the grid
        coord = plane.getPos()
        self.validate_coordinate(coord)
        pcells = plane.getPlaneCells()
        for x in pcells:
            r = x[0]
            c = x[1]
            if r < 0 or r > 7:
                raise Exception("Plane can not be placed in the grid.")
            if c < 0 or c > 7:
                raise Exception("Plane can not be placed in the grid.")
    
class RepositoryValidator():
    
    def __init__(self):
        pass
    
    @staticmethod
    def validate_overlapping(plane, matrix):
        pcells = plane.getPlaneCells()
        for x in pcells:
            r = x[0]
            c = x[1]
            if matrix[r][c] != -1:
                raise Exception("Planes are overlapping!")
            