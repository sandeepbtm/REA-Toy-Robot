"""
    Code created by:
    :type Sandeep Kewlani
"""

import math

class FirstPosition(object):
    """
        This class used for
          robot position the robot.

        :param - x , y
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, FirstPosition):
            return (int(self.x) == int(other.x)) and (int(self.y) == int(other.y))
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, FirstPosition):
            return not (self == other)
        return NotImplemented

    def __add__(self, other):
        x = int(self.x) + int(other.x)
        y = int(self.y) + int(other.y)
        return self.__class__(x, y)


    def x(self, value):
        self.x = int(value)


    def y(self, value):
        self.y = int(value)

class TablePlace(FirstPosition):
    def __mul__(self, scale):
        x = self.x*scale
        y = self.y*scale
        return self.__class__(x, y)

    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)

class TableSize(object):
    def __init__(self, position1, position2):
        self._top = max(position1.y, position2.y)
        self._right = max(position1.x, position2.x)
        self._bottom = min(position1.y, position2.y)
        self._left = min(position1.x, position2.x)

    @property
    def top(self):
        return self._top

    @property
    def right(self):
        return self._right

    @property
    def bottom(self):
        return self._bottom

    @property
    def left(self):
        return self._left

    def contains(self, point):
        contains_x = (int(self._left) <= int(point.x)) and (int(point.x) <= int(self._right))
        contains_y = (int(self._bottom) <= int(point.y)) and (int(point.y) <= int(self._top))
        return contains_x and contains_y