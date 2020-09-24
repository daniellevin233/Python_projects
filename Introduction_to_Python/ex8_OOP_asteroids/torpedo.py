
####################
# Class definition #
####################

class Torpedo:

    TORPEDO_RADIUS = 4
    START_TORPEDO_AGE = 0

    def __init__(self, loc_x, speed_x, loc_y, speed_y, heading):
        """
        The constructor of the Torpedo
        :param loc_x: coordinate of torpedo on the screen by axis x
        :param speed_x: speed of torpedo on the screen by axis x
        :param loc_y: coordinate of torpedo on the screen by axis y
        :param speed_y: speed of torpedo on the screen by axis y
        :param heading: heading of the torpedo
        """
        self.__loc_x = loc_x
        self.__speed_x = speed_x
        self.__loc_y = loc_y
        self.__speed_y = speed_y
        self.__heading = heading
        self.__age = self.START_TORPEDO_AGE

    def torp_is_die(self, life_time):
        """
        Method checks if the torpedo is still live or not
        :param life_time: the life time of the torpedo in the game
        :return: True if torpedo age less then life_time
        False otherwise
        """
        self.__age += 1
        if self.__age >= life_time:  # torpedo've died((
            return True
        else:
            return False

    #######################
    # getters and setters #
    #######################

    def get_loc_x(self):
        """
        :return: integer - coordinate of ship by axis y
        """
        return self.__loc_x

    def get_speed_x(self):
        """
        :return: integer - speed of torpedo by axis x
        """
        return self.__speed_x

    def get_loc_y(self):
        """
        :return: integer - coordinate of torpedo by axis y
        """
        return self.__loc_y

    def get_speed_y(self):
        """
        :return: integer - speed of torpedo by axis y
        """
        return self.__speed_y

    def get_heading(self):
        """
        :return: float - degrees - heading of the torpedo
        """
        return self.__heading

    def get_radius(self):
        """
        :return: float - torpedo radius
        """
        return self.TORPEDO_RADIUS

    def set_loc_x(self, new_loc_x):
        """
        Method sets the coordinate of torpedo by axis x
        :param new_loc_x: float - new coordinate for setting by axis x
        """
        self.__loc_x = new_loc_x

    def set_loc_y(self, new_loc_y):
        """
        Method sets the coordinate of ship by axis y
        :param new_loc_y: float - new coordinate for setting by axis y
        """
        self.__loc_y = new_loc_y
