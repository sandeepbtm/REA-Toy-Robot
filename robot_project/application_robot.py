"""
    Code created by:
    :type Sandeep Kewlani
"""

from table_position import FirstPosition
from robot_direction import RobotDirection
from robot import Robot

class RobotApplication(object):
    """
        This class used for
          robot functionality.
          methods take parameters
          return the response.
          :param - params

    """
    _params = []

    def __init__(self, params=None):
        """Return a RobotApplication class object with params property """
        self.params = params

    @property
    def params(self):
        return self.params

    @params.setter
    def params(self, values):
        self._params = values


    def place_robot(self,values):
        """
            Set the position and direction of robot
            :return RobotApplication Object
        """
        try:
            Robot._position = FirstPosition(values[0], values[1])
            Robot._direction = RobotDirection(values[2])
            return RobotApplication(self)
        except Exception as e:
            print(str(e))

    def robot_methods(self):
        """
            This method is used for getting the object of RobotApplication
            :return RobotApplication:
        """
        try:
            return RobotApplication(self)
        except Exception as e:
            print(str(e))

    def invokePlace(self, target):
        target.place(Robot._position, Robot._direction)
    def invokeMove(self, target):
        target.move_by(1)
    def invokeLeft(self, target):
        target.turn_by(-1)
    def invokeRight(self, target):
        target.turn_by(1)
    def invokeReport(self, target):
        print("Output of the report: %s" % target.report())