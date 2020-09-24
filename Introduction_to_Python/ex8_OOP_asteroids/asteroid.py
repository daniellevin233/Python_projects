###########
# imports #
###########

import math as m

####################
# Class definition #
####################

class Asteroid:

    SIZE_COEFF = 10
    NORM_FACTOR = -5

    def __init__(self, loc_x, speed_x, loc_y, speed_y, size):
        """
        The constructor of the Asteroid
        :param loc_x: coordinate of asteroid on the screen by axis x
        :param speed_x: speed of asteroid on the screen by axis x
        :param loc_y: coordinate of asteroid on the screen by axis y
        :param speed_y: speed of asteroid on the screen by axis y
        :param size: size of asteroid
        """
        self.__loc_x = loc_x
        self.__speed_x = speed_x
        self.__loc_y = loc_y
        self.__speed_y = speed_y
        self.__size = size
        self.__radius = self.set_radius()

    def has_intersection(self, obj):
        """
        Method checks if asteroid intersects with a given obj
        :param obj: the object that we gonna check intersection with
        :return: True if asteroid intersects with an obj; False otherwise
        """
        distance = m.sqrt((obj.get_loc_x() - self.__loc_x)**2 +
                          (obj.get_loc_y() - self.__loc_y)**2)
        if distance <= self.__radius + obj.get_radius():
            return True
        else:
            return False

    #######################
    # getters and setters #
    #######################

    def get_loc_x(self):
        """
        :return: integer - coordinate of asteroid by axis x
        """
        return self.__loc_x

    def get_speed_x(self):
        """
        :return: float - speed of asteroid by axis x
        """
        return self.__speed_x

    def get_loc_y(self):
        """
        :return: integer - coordinate of asteroid by axis y
        """
        return self.__loc_y

    def get_speed_y(self):
        """
        :return: float - speed of asteroid by axis y
        """
        return self.__speed_y

    def get_size(self):
        """
        :return: integer - size of asteroid
        """
        return self.__size

    def get_radius(self):
        """
        :return: float - asteroid radius
        """
        return self.__radius

    def set_loc_x(self, new_loc_x):
        """
        Method sets the coordinate of asteroid by axis x
        :param new_loc_x: float - new coordinate for setting by axis x
        """
        self.__loc_x = new_loc_x

    def set_loc_y(self, new_loc_y):
        """
        Method sets the coordinate of asteroid by axis y
        :param new_loc_y: float - new coordinate for setting by axis y
        """
        self.__loc_y = new_loc_y

    def set_speed_x(self, new_speed_x):
        """
        Method sets the speed of asteroid by axis x
        :param new_speed_x: float - new coordinate for setting by axis x
        """
        self.__speed_x = new_speed_x

    def set_speed_y(self, new_speed_y):
        """
        Method sets the speed of asteroid by axis y
        :param new_speed_y: float - new coordinate for setting by axis y
        """
        self.__speed_y = new_speed_y

    def set_radius(self):
        """
        Method sets the radius of the asteroid
        :return: float - radius of the asteroid
        """
        return self.__size * self.SIZE_COEFF + self.NORM_FACTOR
