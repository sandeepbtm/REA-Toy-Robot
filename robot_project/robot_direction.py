from robot_assignment.table_position import TablePlace

class InvalidDirectionError(Exception):
    pass

class RobotDirection(object):
    """
            This class used for
              robot direction methods.

            :param - vector,value
            :raise - InvalidDirectionError

    """
    VALUES = ['NORTH', 'EAST', 'SOUTH', 'WEST']
    NORTH, EAST, SOUTH, WEST = VALUES
    DIRECTIONS = {
        NORTH: TablePlace(0, 1),
        EAST: TablePlace(1, 0),
        SOUTH: TablePlace(0, -1),
        WEST: TablePlace(-1, 0),
    }

    def __init__(self, value):
        if value not in self.VALUES:
            raise InvalidDirectionError('Invalid direction: "%s"' % value)
        self._value = value

    def __eq__(self, other):
        if isinstance(other, RobotDirection):
            return (self.value == other.value)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, RobotDirection):
            return not (self == other)
        return NotImplemented

    @property
    def vector(self):
        return self.DIRECTIONS[self._value]

    @property
    def value(self):
        return self._value

    def turn_by(self, step):
        index = self.VALUES.index(self._value)
        new_index = (index + step) % len(self.VALUES)
        new_value = self.VALUES[new_index]
        return self.__class__(new_value)