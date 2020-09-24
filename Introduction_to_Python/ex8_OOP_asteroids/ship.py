
####################
# Class definition #
####################

class Ship:

    TURN_ANGLE = 7
    SHIP_RADIUS = 1

    def __init__(self, loc_x, speed_x, loc_y, speed_y, heading=0):
        """
        The constructor of the Ship
        :param loc_x: coordinate of ship on the screen by axis x
        :param speed_x: speed of ship on the screen by axis x
        :param loc_y: coordinate of ship on the screen by axis y
        :param speed_y: speed of ship on the screen by axis y
        :param heading: heading of the ship
        """
        self.__loc_x = loc_x
        self.__speed_x = speed_x
        self.__loc_y = loc_y
        self.__speed_y = speed_y
        self.__heading = heading

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
        :return: float - speed of ship by axis x
        """
        return self.__speed_x

    def get_loc_y(self):
        """
        :return: integer - coordinate of ship by axis y
        """
        return self.__loc_y

    def get_speed_y(self):
        """
        :return: float - speed of ship by axis x
        """
        return self.__speed_y

    def get_heading(self):
        """
        :return: float - degrees - heading of the ship
        """
        return self.__heading

    def get_radius(self):
        """
        :return: float - ship radius
        """
        return self.SHIP_RADIUS

    def set_loc_x(self, new_loc_x):
        """
        Method sets the coordinate of ship by axis x
        :param new_loc_x: float - new coordinate for setting by axis x
        """
        self.__loc_x = new_loc_x

    def set_loc_y(self, new_loc_y):
        """
        Method sets the coordinate of ship by axis y
        :param new_loc_y: float - new coordinate for setting by axis y
        """
        self.__loc_y = new_loc_y

    def set_speed_x(self, new_speed_x):
        """
        Method sets the speed of ship by axis x
        :param new_speed_x: float - new speed by axis x for setting
        """
        self.__speed_x = new_speed_x

    def set_speed_y(self, new_speed_y):
        """
        Method sets the speed of ship by axis y
        :param new_speed_y: float - new speed by axis y for setting
        """
        self.__speed_y = new_speed_y

    def set_heading(self, onclock=False):
        """
        Method sets the heading for the ship
        :param onclock: the boolean parameter defining if ship need turn
        on clock direction - True, contrary to clock direction - False
        """
        if onclock:
            self.__heading -= self.TURN_ANGLE
        else:
            self.__heading += self.TURN_ANGLE
