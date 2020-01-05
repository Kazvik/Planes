import unittest
from domain.plane import Plane
from validators import PlaneValidator, RepositoryValidator
from repository import Repo

class TestPlane(unittest.TestCase):
    
    def setUp(self):
        self.plane = Plane("C1", "up")
    
    def test_getPos(self):
        assert(self.plane.getPos() == "C1")
    
    def test_getOrientation(self):
        assert(self.plane.getOrientation() == "up")
    
    def test_getPlaneCells(self):
        planeCells = self.plane.getPlaneCells()
        assert(planeCells[0] == (0,2))
        assert(planeCells[1] == (1,0))
        assert(planeCells[2] == (1,1))
        assert(planeCells[3] == (1,2))
        assert(planeCells[4] == (1,3))
        assert(planeCells[5] == (1,4))
        assert(planeCells[6] == (2,2))
        assert(planeCells[7] == (3,1))
        assert(planeCells[8] == (3,2))
        assert(planeCells[9] == (3,3))

class TestPlaneValidator(unittest.TestCase):
    
    def setUp(self):
        self.validator = PlaneValidator()
    
    def test_validate_letter(self):
        self.assertRaises(ValueError, lambda:self.validator.validate_letter('K'))
        self.validator.validate_letter('A')
        self.validator.validate_letter('H')
        self.validator.validate_letter('D')
    
    def test_validate_digit(self):
        self.assertRaises(ValueError, lambda:self.validator.validate_digit('9'))
        self.validator.validate_digit('1')
        self.validator.validate_digit('8')
        self.validator.validate_digit('6')
    
    def test_validate_coordinate(self):
        self.assertRaises(ValueError, lambda:self.validator.validate_coordinate('C9'))        
        self.assertRaises(ValueError, lambda:self.validator.validate_coordinate('K3')) 
    
    def test_validate_place(self):
        p = Plane("C1", "down")
        self.assertRaises(Exception, lambda:self.validator.validate_place(p))
        p = Plane("C1", "up")
        self.validator.validate_place(p)

class TestRepositoryAndRepositoryValidator(unittest.TestCase):

    def setUp(self):
        self.validator = RepositoryValidator()
        self.repo = Repo(self.validator)
        
    def test_repo(self):
        p = Plane("C1", "up")
        self.repo.add(p)   
         

if __name__ == "__main__":
    unittest.main()