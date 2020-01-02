from copy import deepcopy

class Repo():
    
    def __init__(self, RepoValidator):
        #function that initializes the a repository
        self._planes = self.generate()
        self._shots = self.generate()
        self._validator = RepoValidator
        
    @staticmethod
    def generate():
        #function that generates an 8x8 grid
        #it returns the grid filled with '-1' values
        m = []
        row = [-1] * 8
        for i in range(8):
            m += [deepcopy(row)]
        return m        

    def shotsGrid(self):
        #function that returns the shot grid of a repository
        return self._shots
    
    def planesGrid(self):
        #function that returns the planes grid of a repository
        return self._planes
    
    def add(self, plane):
        #function that adds a new plane to the repo
        self._validator.validate_overlapping(plane, self._planes)
        pcells = plane.getPlaneCells()
        for x in pcells:
            r = x[0]
            c = x[1]
            l = self._planes[r]
            l[c] = 1
            self._planes[r] = l
    
    def hit(self, row, column):
        #function that changes the values of a plane cell from '1' to '0' if it was hit
        if self._planes[row][column] == 1:
            self._planes[row][column] = 0
    
    def markGoodShot(self, row, column):
        #function that marks a successfull shot in the shots grid
        self._shots[row][column] = 1
    
    def markBadShot(self, row, column):
        #function that marks a missed shot in the shots grid
        self._shots[row][column] = 0
    
    def checkPlaneCell(self, row, column):
        #function that check how a cell is from the plane grid
        return self._planes[row][column]
    