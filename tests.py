import unittest
from domain.plane import Plane
from validators import PlaneValidator, RepositoryValidator
from repository import Repo
from imports.queue import Queue
from controllers.playerController import PlayerController
from controllers.computerController import ComputerController

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
        p = Plane("C1", "up")
        self.repo.add(p)   
        
    def test_add(self):
        p2 = Plane("D6", "right")
        self.assertRaises(Exception, lambda:self.repo.add(p2))
    
    def test_markGoodShot(self):
        self.repo.markGoodShot(1,4)
        assert(1 == self.repo.shotsGrid()[1][4])
    
    def test_markBadShot(self):
        self.repo.markBadShot(1,4)
        assert(0 == self.repo.shotsGrid()[1][4])
    
class TestQueue(unittest.TestCase):
    
    def setUp(self):
        self.q = Queue()
    
    def test_queue(self):
        self.q.push(5)
        assert(self.q.pop() == 5)
        self.q.push(6)
        assert(self.q.size() == 1)
        self.q.clear()
        
        assert(self.q.size() == 0)
        
class TestPlayerController(unittest.TestCase):
    
    def setUp(self):
        self.validator = PlaneValidator()
        self.repo = Repo(self.validator)
        self.controller = PlayerController(self.repo, self.validator)
        self.controller.addPlane("C1", "up")
    
    def test_controller(self):
        assert(self.controller.getNoPlanes() == 1)

class TestComputerController(unittest.TestCase):
    
    def setUp(self):
        self.validator = PlaneValidator()
        self.repo = Repo(self.validator)
        self.controller = ComputerController(self.repo, self.validator)
    
    def test_controller(self):
        assert(self.controller.getNoPlanes() == 2)
        
        

if __name__ == "__main__":
    unittest.main()