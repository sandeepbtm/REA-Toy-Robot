class MoveOutOfBoundsError(Exception):
    pass

class MissingPlaceError(Exception):
    pass

class Robot(object):
    """
        This class used for
          robot position and direction set.

        :param - table,position,direction
        :raise - MissingPlaceError

    """
    def __init__(self, table):
        self._table = table
        self._position = None
        self._direction = None

    @property
    def table(self):
        return self._table

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        if not self._table.rect.contains(position):
            raise MoveOutOfBoundsError('Unable to move Robot Moves are not allowed. 0 - 4')

        self._position = position

    @property
    def direction(self):
        return self._direction

    @direction.setter
    def direction(self, direction):
        self._direction = direction

    def place(self, position, direction):
        self.position = position
        self.direction = direction

    def move_by(self, step):
        if not self._position:
            raise MissingPlaceError('Unable to move Robot until placed')

        new_position = self._position + (self._direction.vector * step)
        self.position = new_position

    def turn_by(self, step):
        if not self._direction:
            raise MissingPlaceError('Unable to turn Robot until placed')

        new_drection = self._direction.turn_by(step)
        self.direction = new_drection

    def report(self):
        if not self._direction:
            raise MissingPlaceError('Unable to report Robot until placed')

        return ("%s,%s,%s" % (self._position.x, self._position.y, self._direction.value))