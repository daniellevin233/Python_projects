############################################################
# Helper class
############################################################
AXIS_X = 0
AXIS_Y = 1

class Direction:
    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT, RIGHT,
    NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but all other
    implementations are for you to carry out.
    """
    UP = 2
    DOWN = 8
    LEFT = 4
    RIGHT = 6

    NOT_MOVING = -1

    VERTICAL = 0
    HORIZONTAL = 1

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)

############################################################
# Class definition
############################################################

class Car:
    """
    A class representing a car in rush hour game.
    A car is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A car drives on its vertical\horizontal axis back and
    forth until reaching the board's boarders. A car can only drive to an empty
    slot (it can't override another car).
    """

    MAIN_CAR_COL = 'R'
    MAIN_CAR_LEN = 2

    def __init__(self, color, length, location, orientation):
        """
        A constructor for a Car object
        :param color: A string representing the car's color
        :param length: An int in the range of (2,4) representing the car's length.
        :param location: A tuple representing the car's head (x, y) location
        :param orientation: An int representing the car's orientation
        """
        self.__color = color
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def create_car_coordinates_lst(self):
        """
        Method creates list of tuples that signify all coordinates
        that car takes on the board.
        :return: List of tuples with car's locations coordinates
        """
        loc_x, loc_y = self.__location
        locations_lst = []
        for i in range(self.__length):
            if self.__orientation == Direction.VERTICAL:
                new_loc_tuple = (loc_x + 1, loc_y + i)
            else:
                new_loc_tuple = (loc_x + i + 1, loc_y)
            locations_lst.append(new_loc_tuple)
        return locations_lst

    def moved_car_location(self, direction):
        """
        Method creates new location of the car after moving in accordance to
        given direction
        :param direction: Direction for moving the car
        :return: tuple representing changed location
        """
        loc_x, loc_y = self.__location[AXIS_X], self.__location[AXIS_Y]
        if direction == Direction.RIGHT:
            loc_x += 1
        elif direction == Direction.LEFT:
            loc_x -= 1
        elif direction == Direction.DOWN:
            loc_y += 1
        else:
            loc_y -= 1
        new_location = (loc_x, loc_y)
        return new_location

    def get_color(self):
        """
        :return: string that contains color of the car
        """
        return self.__color

    def get_length(self):
        """
        :return: integer - the length of the car
        """
        return self.__length

    def get_location(self):
        """
        :return: tuple - pair of coordinates for car location
        """
        return self.__location

    def get_orientation(self):
        """
        :return: integer: 0 if vertical, 1 - horizontal orientation
        """
        return self.__orientation

    def set_if_car_orientation_is_good_for_direction(self, direction):
        """
        Method checks if the chosen directions of moving is possible
        for current car
        :param direction: direction that user want to move the car
        :return: True if given direction satisfies the car orientation
        False otherwise
        """
        if (self.__orientation == Direction.VERTICAL) and \
                (direction in [Direction.UP, Direction.DOWN]):
            return True
        elif (self.__orientation == Direction.HORIZONTAL) and \
                (direction in [Direction.LEFT, Direction.RIGHT]):
            return True
        else:
            return False
