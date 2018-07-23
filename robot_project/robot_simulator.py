"""
    Code created by:
    :type Sandeep Kewlani
"""

from robot import Robot, MoveOutOfBoundsError, MissingPlaceError
from table import Table
from robot_command import CommandParser
from application_robot import RobotApplication

class RobotSimulation(object):
    """
        This class used for
        robot simulating and running the whole application.
    """
    def __init__(self):
        self.command_parser = CommandParser()
        self.reset()

    def reset(self):
        self.table = Table(5, 5)
        self.robot = Robot(self.table)

    def run(self, line):
        command = self.command_parser.parse(line)
        command,method = command.split(",")
        try:
            command = RobotApplication(command)
            self.method_invoke(command,method)
        except MoveOutOfBoundsError as e:
            raise MoveOutOfBoundsError("There is out of bound error, because "
                                       "robot is allowed to move within 5*5 units i.e. 0 to 4. "
                                       "Only 4 moves allowed at a time,If robot place on 0*0. "
                                       "Correct your input data.")
        except MissingPlaceError as e:
            raise MissingPlaceError("Robot is not placed,Place the robot first within 5*5 dimensions.")

    def method_invoke(self,command,method):
        if method == "invokePlace":
            command.invokePlace(target=self.robot)
        elif method == "invokeMove":
            command.invokeMove(target=self.robot)
        elif method == "invokeLeft":
            command.invokeLeft(target=self.robot)
        elif method == "invokeRight":
            command.invokeRight(target=self.robot)
        elif method == "invokeReport":
            command.invokeReport(target=self.robot)
        else:
            print("Given method is not available to call.")