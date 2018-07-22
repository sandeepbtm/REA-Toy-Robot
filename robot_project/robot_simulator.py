from robot_project.robot import Robot, MoveOutOfBoundsError, MissingPlaceError
from robot_project.table import Table
from robot_project.robot_command import CommandParser
from robot_project.application_robot import *

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
            print ('Skip %s:' % command.identifier, e)
        except MissingPlaceError as e:
            print('Skip %s:' % command.identifier, e)

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