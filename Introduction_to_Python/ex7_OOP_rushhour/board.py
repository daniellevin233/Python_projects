############################################################
# Imports
############################################################
import game_helper as gh
from car import Car, Direction

############################################################
# Constants
############################################################

DELIMITER = ''

############################################################
# Class definition
############################################################

class Board:
    """
    A class representing a rush hour board.
    """
    AXIS_X = 0  # axis x will be first in tuples
    AXIS_Y = 1  # axis y will be second in tuples
    EXIT_LETTER = 'E'
    EMPTY_SQUARE = '_'
    ADD_CAR_SUCCESS_MSG = '\nA car was added successfully!\n'
    ADD_CAR_FAILURE_MSG = '\nAdding car failed, try another parameters\n'
    CAR_MOVE_SUCCESS_MSG = '\nThe car was moved successfully!\n'
    ERROR_ORIENTATION_MSG = 'Choose UP or DOWN for vertical car,' \
                            ' LEFT or RIGHT for horizontal one\n'
    OUT_OF_BOUND_MSG = 'The car got out of bound, try again with ' \
                       'another parameters\n'
    OCCUPIED_SQUARE_MSG = 'The desired square is occupied, try again ' \
                          'with another parameters\n'
    MOVE_ERROR_MSG = '\nMoving car is failed.\n'

    def __init__(self, cars, exit_board, size=6):
        """
        Initialize a new Board object.
        :param cars: A list (or dictionary) of cars.
        :param size: Size of board (Default size is 6).
        """
        self.__cars = cars
        self.__exit_board = exit_board
        self.__size = size
        self.__valid_colors = gh.VALID_COLORS  # copy the colors set
        self.__board_lst2d = self.__create_start_board_lst2d__()
        # create the board_lst2d to start

    def add_car(self, car):
        """
        Add a single car to the board.
        If the error was found, accordant error message will be printed
        :param car: A car object
        :return: True if a car was successfully added, False otherwise.
        """
        car_coordinates = car.create_car_coordinates_lst()
        # declare list of tuples that contain coordinates of given car
        for cur_coord in car_coordinates:
            real_coord = (cur_coord[self.AXIS_X], cur_coord[self.AXIS_Y])
            # add 1 to axis_x hence first column is not part of the board
            if not self.coord_is_in_board(real_coord):
                print(self.OUT_OF_BOUND_MSG)
                return False
            if not self.is_empty(real_coord):
                print(self.OCCUPIED_SQUARE_MSG)
                return False
        else:
            self.__add_car_to_board_lst2d(car_coordinates, car)
            return True

    def coord_is_in_board(self, coord):
        """
        Method checks if given coordinate is inside the board
        :param coord: tuple - (x, y) - coordinate for checking
        :return: False if coordinate is out of the board, True otherwise
        """
        x_coord, y_coord = coord
        if x_coord > self.__size or y_coord > self.__size \
                or x_coord < 0 or y_coord < 0:
            return False
        else:
            return True

    def is_empty(self, location):
        """
        Check if a given location on the board is free.
        :param location: x and y coordinates of location to be check
        :return: True if location is free, False otherwise
        """
        x_coord, y_coord = location
        if self.__board_lst2d[y_coord][x_coord] != self.EMPTY_SQUARE:
            # the only empty squares on the board are '_'
            return False
        else:
            return True

    def place_main_car_on_board(self):
        """
        This method maps the main car on the board
        """
        main_car_location = (self.__exit_board[self.AXIS_X], 0)  # start
        # position is always the exit x coordinate of the axis x
        # and is always on 0 coordinate of axis y
        main_car = Car(Car.MAIN_CAR_COL, Car.MAIN_CAR_LEN, main_car_location,
                       Direction.VERTICAL)
        self.__cars[Car.MAIN_CAR_COL] = main_car  # renew the dict
        self.add_car(main_car)
        self.__valid_colors.remove(Car.MAIN_CAR_COL)

    def place_cars_on_board(self):
        """
        This method maps the car on the board in accordance to input
        parameters that will be given inside the method
        :return: False if car with given parameters can't be added
        True if car can be added
        """
        color, length, location, orientation = gh.get_car_input(self.__size)
        new_car = Car(color, length, location, orientation)
        self.__cars[color] = new_car
        if not self.add_car(new_car):
            return False
        else:
            self.__valid_colors.remove(color)  # extract the chosen color
            return True

    def move(self, car, direction):
        """
        Move a car in the given direction.
        :param car: A Car object to be moved.
        :param direction: A Direction object representing desired direction
            to move car.
        :return: True if movement was possible and car was moved, False otherwise.
        """
        if not car.set_if_car_orientation_is_good_for_direction \
                    (direction):
            print(self.MOVE_ERROR_MSG)
            print(self.ERROR_ORIENTATION_MSG)
            return False
        new_car_location = car.moved_car_location(direction)
        # create new car location after potential moving
        potentially_moved_car = Car(car.get_color(), car.get_length(),
                                    new_car_location, car.get_orientation())
        # create object of type Car -
        # car that user potentially want to make, then check if it's possible
        self.__clean_car_from_board(car)  # clean the old car for now
        if not self.add_car(potentially_moved_car):
            print(self.MOVE_ERROR_MSG)
            # moving failed
            self.add_car(car)  # we need to return the cleaned car
            return False
        else:
            # success moving, renew the cars_dict
            self.__renew_cars_dict(potentially_moved_car)
            print(self.CAR_MOVE_SUCCESS_MSG)
            return True

    def __renew_cars_dict(self, car):
        """
        Method puts the given car in cars_dict with key 'color' of this car
        :param car: Object of type Car that we gonna put in dictionary
        :return: None
        """
        self.__cars[car.get_color()] = car

    def __clean_car_from_board(self, car):
        """
        This method cleans the car from the board, i.e. change cars'
        squares by '_'
        :param car: the object of type Car that we gonna clean
        :return: None
        """
        car_coordinates = car.create_car_coordinates_lst()
        for cur_coord in car_coordinates:
            x_coord, y_coord = cur_coord[self.AXIS_X], cur_coord[self.AXIS_Y]
            self.__board_lst2d[y_coord][x_coord] = self.EMPTY_SQUARE

    def __create_start_board_lst2d__(self):
        """
        Method creates the 2 dimensional list that represents the
        game board in the beginning of the game
        :return: Two dimensional list, every internal list represents
        string of the board
        """
        start_board_lst_2d = []
        for i in range(self.__size):  # first print the strings of the board
            board_str_lst = [str(i)]
            for j in range(self.__size):
                board_str_lst.append(self.EMPTY_SQUARE)
            start_board_lst_2d.append(board_str_lst)
        board_last_str_lst = ['-']  # here we gonna print the last
        # string on the board
        for k in range(self.__size):
            if k == self.__exit_board[self.AXIS_X]:
                board_last_str_lst.append(self.EXIT_LETTER)
            else:
                board_last_str_lst.append(str(k))
        start_board_lst_2d.append(board_last_str_lst)
        return start_board_lst_2d

    def __add_car_to_board_lst2d(self, car_coord, car):
        """
        This method add to the board car on its coordinates,
        that given as param. Meaning: the letter that signify current car
        car_coord: list of tuples, contain all car coordinates on the board
        :return: None
        """
        for cur_coord in car_coord:
            x_coord, y_coord = cur_coord[self.AXIS_X], cur_coord[self.AXIS_Y]
            self.__board_lst2d[y_coord][x_coord] = car.get_color()

    def main_car_got_exit(self):
        """
        This method checks if the main car is got to the exit
        :return: True if main car color is one square before the exit,
        False otherwise
        """
        exit_x, exit_y = self.__exit_board[self.AXIS_X] + 1, \
                         self.__exit_board[self.AXIS_Y]
        # add +1 to x_coord hence first column os not part of the board
        if self.__board_lst2d[exit_y][exit_x] == Car.MAIN_CAR_COL:
            return True
        else:
            return False

    def get_cars_dict(self):
        """
        :return: dictionary of cars with colors as keys
        """
        return self.__cars

    def __repr__(self):
        """
        :return: Return a string representation of the board.
        """
        board_repr = DELIMITER
        for string in self.__board_lst2d:
            board_repr += str(string) + '\n'
        return board_repr
