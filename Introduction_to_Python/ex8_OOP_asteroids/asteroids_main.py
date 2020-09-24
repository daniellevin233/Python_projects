##############################################################################
# FILE : ex8.py
# WRITER : Daniel Levin , daniellevin , 336462874
# EXERCISE : intro2cs ex8 2017-2018
# DESCRIPTION: Game Asteroids with OOP, classes: GameRunner, Ship,
# Asteroid, Torpedo
##############################################################################

###########
# imports #
###########

from screen import Screen
import sys
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import random as rndm
import math as m

#####################
# default constants #
#####################

DEFAULT_ASTEROIDS_NUM = 3

####################
# Class definition #
####################

class GameRunner:

    # general parameters of the game #
    START_USER_POINTS = 0
    MAX_POINTS_VALUE = 100
    MEDIUM_POINTS_VALUE = 50
    MIN_POINTS_VALUE = 20

    # parameters of torpedo #
    ACCELERATION_FACTOR = 2
    TORPEDO_LIFE_TIME = 200

    # parameters of ship #
    START_SHIP_LIVES = 3
    START_SHIP_SPEED_X = START_SHIP_SPEED_Y = 0
    MAX_TORPEDOES_AMOUNT = 15

    # parameters of asteroids
    MAX_ASTEROID_SIZE, MIN_ASTEROID_SIZE = 3, 1
    AST_SIZES_LST = [3]  # if user wants to add asteroids of different sizes
    # that will be chosen randomly, he can change this list
    ASTEROID_SPEEDS_LST = [1, 2, 3, 4]  # the same for the speeds

    def __init__(self, asteroids_amnt):
        """
        The main constructor of class GameRunner
        :param asteroids_amnt: Amount of asteroids for adding to game
        """
        self._screen = Screen()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.delta_x = self.screen_max_x - self.screen_min_x
        self.delta_y = self.screen_max_y - self.screen_min_y
        self.ast_amnt = asteroids_amnt
        self.ship = self.__create_ship()  # the main ship of the game
        self._init_asteroids_lst()
        self.torp_lst = []  # the list of torpedoes
        self.user_points = self.START_USER_POINTS
        self.ship_lifes = self.START_SHIP_LIVES

    def _init_asteroids_lst(self):
        """
        Constructor for list of asteroids
        """
        self.ast_lst = []
        for i in range(self.ast_amnt):
            size = rndm.choice(self.AST_SIZES_LST)
            new_ast = self.__create_asteroid(size)
            self.ast_lst.append(new_ast)
            self._screen.register_asteroid(new_ast, new_ast.get_size())

    def run(self):
        """
        Method that runs the game process.
        """
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        """
        Method that manage the loop of the game.
        """
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        This method represents loop of the game, every loop next things happen:
        Drawing, moving the objects, treating the buttons pressing
        Checking the game finish conditions etc...
        """
        if self.__game_is_finished():  # check if the game has to be finished
            self._screen.end_game()
            sys.exit()
        # first draw the ship and refresh its properties
        self._screen.draw_ship(self.ship.get_loc_x(),
                               self.ship.get_loc_y(), self.ship.get_heading())
        self.__move_object(self.ship)
        self.__set_ship_heading()
        self.__accelerate_ship()
        # condition for creating the torpedo
        if self._screen.is_space_pressed() and \
                len(self.torp_lst) < self.MAX_TORPEDOES_AMOUNT:
            self.__create_torpedo()
        for cur_ast in self.ast_lst:
            # here working with asteroids
            self._screen.draw_asteroid(cur_ast, cur_ast.get_loc_x(),
                                       cur_ast.get_loc_y())
            self.__move_object(cur_ast)
            self.__check_ast_with_ship_intersection(cur_ast)
            for cur_torp in self.torp_lst:
                # now work with torpedoes
                self._screen.draw_torpedo(cur_torp, cur_torp.get_loc_x(),
                                cur_torp.get_loc_y(), cur_torp.get_heading())
                self.__move_object(cur_torp)
                self.__check_ast_with_torp_intersection(cur_ast, cur_torp)
                if cur_torp.torp_is_die(self.TORPEDO_LIFE_TIME):
                    self._screen.unregister_torpedo(cur_torp)
                    self.torp_lst.remove(cur_torp)

    def __create_ship(self):
        """
        Method creates the ship for the game, coordinates are chosen randomly.
        :return: object of type Ship - ship of the game
        """
        loc_x = rndm.randint(self.screen_min_x, self.screen_max_x)
        loc_y = rndm.randint(self.screen_min_y, self.screen_max_y)
        ship = Ship(loc_x, self.START_SHIP_SPEED_X,
                    loc_y, self.START_SHIP_SPEED_Y)
        return ship

    def __create_asteroid(self, size):
        """
        This method creates one asteroid in the game. Coordinates and speed
        are chosen randomly from constant parameters of the class GameRunner.
        :param size: integer - size of the asteroid that we gonna create
        :return: object of type Asteroid - new asteroid in the game
        """
        loc_x = rndm.randint(self.screen_min_x, self.screen_max_x)
        loc_y = rndm.randint(self.screen_min_y, self.screen_max_y)
        speed_x = rndm.choice(self.ASTEROID_SPEEDS_LST)
        speed_y = rndm.choice(self.ASTEROID_SPEEDS_LST)
        asteroid = Asteroid(loc_x, speed_x, loc_y, speed_y, size)
        while asteroid.has_intersection(self.ship):  # check the place if it's
            # possible to draw asteroid there
            loc_x = rndm.randint(self.screen_min_x, self.screen_max_x)
            loc_y = rndm.randint(self.screen_min_y, self.screen_max_y)
        asteroid = Asteroid(loc_x, speed_y, loc_y, speed_y, size)
        return asteroid

    def __create_torpedo(self):
        """
        This method creates one torpedo of the game. Here formula for the
        speed, location and heading are these of the ship in the moment
        of striking.
        """
        speed_x = self.ship.get_speed_x() + self.ACCELERATION_FACTOR * \
                  m.cos(m.radians(self.ship.get_heading()))
        speed_y = self.ship.get_speed_y() + self.ACCELERATION_FACTOR * \
                  m.sin(m.radians(self.ship.get_heading()))
        torp = Torpedo(self.ship.get_loc_x(), speed_x,
                       self.ship.get_loc_y(), speed_y,
                       self.ship.get_heading())
        self._screen.register_torpedo(torp)
        self.torp_lst.append(torp)

    def __move_object(self, obj):
        """
        This method move the given object on the screen by setting new
        coordinates after activating the formula on them.
        :param obj: the object for moving
        """
        new_coord_x = (obj.get_speed_x() + obj.get_loc_x() - self.screen_min_x)\
                      % self.delta_x + self.screen_min_x
        new_coord_y = (obj.get_speed_y() + obj.get_loc_y() - self.screen_min_y)\
                      % self.delta_y + self.screen_min_y
        obj.set_loc_x(new_coord_x)
        obj.set_loc_y(new_coord_y)

    def __accelerate_ship(self):
        """
        This method is responsible for accelerating the ship
        """
        if self._screen.is_up_pressed():  # change the acceleration if proper
            # button was pressed
            head_in_rad = m.radians(self.ship.get_heading())
            # using the method from math library to put degrees in radians
            new_speed_x = self.ship.get_speed_x() + m.cos(head_in_rad)
            new_speed_y = self.ship.get_speed_y() + m.sin(head_in_rad)
            # setting the new values for speed of the ship
            self.ship.set_speed_x(new_speed_x)
            self.ship.set_speed_y(new_speed_y)

    def __set_ship_heading(self):
        """
        Method is responsible for changing the ship heading in the game.
        """
        if self._screen.is_right_pressed():  # the proper button is pressed
            self.ship.set_heading(True)  # for turning on the clock direction
        elif self._screen.is_left_pressed():
            self.ship.set_heading()  # turning against clock direction

    def __check_ast_with_ship_intersection(self, asteroid):
        """
        Method treats case of intersection for the ship and given asteroid (1)
        In case of (1):
        Printing the message of the intersection on the game screen (2)
        Diminishing life of the ship (3) and removing it from the screen (4)
        Then unregistering the bumped asteroid (5)
        :param asteroid: object of type Asteroid that we gonna check
        intersection for.
        """
        if asteroid.has_intersection(self.ship):  # (1)
            self._screen.show_message\
                ('Oops', 'Your spaceship bumped into asteroid( Be careful!')  # (2)
            self.ship_lifes -= 1  # (3)
            self._screen.remove_life()  # (4)
            self._screen.unregister_asteroid(asteroid)  # (5)
            self.ast_lst.remove(asteroid)  # (5)

    def __check_ast_with_torp_intersection(self, asteroid, torpedo):
        """
        Method treats case of intersection for given torpedo
        and given asteroid (1)
        In case of (1):
        Unregistering the torpedo (2)
        Adding game points to the user because of successful striking (3)
        Splitting the asteroid that was striked (4)
        :param asteroid: object of type Asteroid that we gonna check
        intersection with torpedo for
        :param torpedo: object of type Torpedo that we gonna check
        intersection with asteroid for.
        """
        if asteroid.has_intersection(torpedo):  # (1)
            self._screen.unregister_torpedo(torpedo)  # (2)
            self.torp_lst.remove(torpedo)  # (2)
            self.__add_points_to_user(asteroid.get_size())  # (3)
            self.__split_asteroid(asteroid, torpedo)  # (4)

    def __add_points_to_user(self, ast_size):
        """
        Method add points to user for successful striking the asteroid
        :param ast_size: integer - size of striked asteroid
        """
        if ast_size == self.MAX_ASTEROID_SIZE:
            add_points = self.MIN_POINTS_VALUE
        elif ast_size == self.MIN_ASTEROID_SIZE:
            add_points = self.MAX_POINTS_VALUE
        else:
            add_points = self.MEDIUM_POINTS_VALUE
        self.user_points += add_points
        self._screen.set_score(self.user_points)

    def __split_asteroid(self, ast, torp):
        """
        Method splits the beaten asteroid
        :param ast: object of type Asteroid - asteroid that we gonna split
        :param torp: object of type Torpedo - torpedo that beat the asteroid
        """
        # unregister the beaten asteroid
        self._screen.unregister_asteroid(ast)
        self.ast_lst.remove(ast)
        new_ast_speed_x = (torp.get_speed_x() + ast.get_speed_x()) / \
                      m.sqrt(ast.get_speed_x()**2 + ast.get_speed_y()**2)
        new_ast_speed_y = (torp.get_speed_y() + ast.get_speed_y()) / \
                      m.sqrt(ast.get_speed_x()**2 + ast.get_speed_y()**2)
        if ast.get_size() == self.MIN_ASTEROID_SIZE:
            return  # the smallest asteroid isn't given to splitting
        else:  # the size is bigger then minimal, split asteroid
            # to two smaller asteroids by size smaller by 1
            size = ast.get_size() - 1
            # creating two new asteroids
            new_ast_1 = Asteroid(ast.get_loc_x(), new_ast_speed_x,
                                 ast.get_loc_y(), new_ast_speed_y, size)
            new_ast_2 = Asteroid(ast.get_loc_x(), -new_ast_speed_x,
                                 ast.get_loc_y(), -new_ast_speed_y, size)
            self._screen.register_asteroid(new_ast_1, new_ast_1.get_size())
            self._screen.register_asteroid(new_ast_2, new_ast_2.get_size())
            self.ast_lst.append(new_ast_1)
            self.ast_lst.append(new_ast_2)

    def __game_is_finished(self):
        """
        Method checks different cases of game finishing,
        and if one of them was fulfilled print relevant message.
        :return: True if game need to be finished
        False otherwise
        """
        is_finish = False
        if self.ship_lifes == 0:
            self._screen.show_message('LOSE',
                  "You've got out of lives. Good luck next time!" +
                                    "\nYour score: " + str(self.user_points))
            is_finish = True
        elif not self.ast_lst:
            self._screen.show_message('WIN!',
                        "You've destroyed all asteroids. Your score: "
                            + str(self.user_points) + "\nCONGRATULATIONS!")
            is_finish = True
        elif self._screen.should_end():
            self._screen.show_message("Exit", "You've pressed the exit button")
            is_finish = True
        return is_finish

def main(amnt):
    """
    The function creates the GameRunner object representing
    our game
    :param amnt:number of asteroids for the game
    """
    runner = GameRunner(amnt)
    runner.run()

if __name__ == "__main__":
    """The main place of the code that run it on"""
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
