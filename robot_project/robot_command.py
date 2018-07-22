import re
from robot_project.application_robot import *

class InvalidCommandError(Exception):
    pass

class CommandNotFoundError(Exception):
    pass

class CommandParser(object):
    """This class is used for setting up the moves and calling the method of robot.
    :return RobotApplication
    :exception CommandNotFound,InvalidCommand
    :
    """
    def parse(self, line):
        try:
            match = re.match(r"(\w+)( (.*))?", line)
            if not match:
                raise InvalidCommandError('Given command is not valid command in the line "%s"' % line)
            identifier = match.group(1)
            params = (match.group(3) or "").split(',')

            if identifier == "PLACE":
                command = RobotApplication.place_robot(object,params)
                return str(command).__add__(",invokePlace")
            elif identifier == "MOVE":
                command = RobotApplication.robot_methods(object)
                return str(command).__add__(",invokeMove")
            elif identifier == "RIGHT":
                command = RobotApplication.robot_methods(object)
                return str(command).__add__(",invokeRight")
            elif identifier == "LEFT":
                command = RobotApplication.robot_methods(object)
                return str(command).__add__(",invokeLeft")
            elif identifier == "REPORT":
                command = RobotApplication.robot_methods(object)
                return str(command).__add__(",invokeReport")
            else:
                print("Please provide the exact input that is valid for robot. Accepted only - PLACE,MOVE,RIGHT,LEFT,REPORT")

            raise CommandNotFoundError('Given Command not found for this robot movement =  "%s"' % identifier)
        except Exception as e:
            print(str(e))