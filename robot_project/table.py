from robot_project.table_position import FirstPosition, TableSize

class Table(object):
    """
        This class used for initialize
          cardbod size. Define the table size to roam for robot.

        :flow - robot_simulator --> Table --> TableSize-->
        :param - size_x ,size_y
    """
    def __init__(self, size_x, size_y):
        bottom_left = FirstPosition(0, 0)
        top_right = FirstPosition(size_x - 1, size_y -1)
        self.rect = TableSize(bottom_left, top_right)