from copy import deepcopy
class Repo():
    
    def __init__(self, RepoValidator):
        self._planes = self.generate()
        self._shots = self.generate()
        self._validator = RepoValidator
        
    @staticmethod
    def generate():
        m = []
        row = [-1] * 8
        for i in range(8):
            m += [deepcopy(row)]
        return m        

    def shotsGrid(self):
        return self._shots
    
    def planesGrid(self):
        return self._planes
    
    def add(self, plane):
        self._validator.validate_overlapping(plane, self._planes)
        pcells = plane.getPlaneCells()
        for x in pcells:
            r = x[0]
            c = x[1]
            l = self._planes[r]
            l[c] = 1
            self._planes[r] = l
    
    def hit(self, row, column):
        
        if self._planes[row][column] == 1:
            self._planes[row][column] = 0
    
    def markGoodShot(self, row, column):
        self._shots[row][column] = 1
    
    def markBadShot(self, row, column):
        self._shots[row][column] = 0
    
    def checkPlaneCell(self, row, column):
        return self._planes[row][column]
    