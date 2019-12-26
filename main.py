
"""
Description: This is the 'main' module. It handles all the components of the application.
"""
#_______________IMPORT ZONE_______________

from consoles.ui_interface import ConsoleInterface
from controllers.computerController import ComputerController
from controllers.gameController import GameController
from controllers.playerController import PlayerController
from repository import Repo
from validators import PlaneValidator, RepositoryValidator

#validators
planeValidator = PlaneValidator()
repositoryValidator = RepositoryValidator()

# repositories
playerRepo = Repo(repositoryValidator)
computerRepo = Repo(repositoryValidator)

# controllers
playerController = PlayerController(playerRepo, planeValidator)
computerController = ComputerController(computerRepo, planeValidator)
gameController = GameController(playerController, computerController)

# interfaces
console = ConsoleInterface(gameController)

if __name__ == "__main__":
    console.runGame()