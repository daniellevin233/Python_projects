##################################################################################
# FILE : ex7.py
# WRITER : Daniel Levin , daniellevin , 336462874
# EXERCISE : intro2cs ex6 2017-2018
# DESCRIPTION: Game "Rush Hour" with OOP, classes: Game, Board, Car, Direction
##################################################################################

############################################################
# Imports
############################################################

import game_helper as gh
from car import Car, Direction
from board import Board

############################################################
# Class definition
############################################################

class Game:
    """
    A class representing a rush hour game.
    A game is composed of cars that are located on a square board and a user
    which tries to move them in a way that will allow the red car to get out
    through the exit
    """
    START_GAME_MSG = 'Welcome to Rush hour game'
    ASK_CAR_COL_MSG = 'What color car would you like to move?'

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.board = board

    def single_turn(self):
        """
        The function runs one round of the game :
            1. Print board to the screen
            2. Get user's input of: what color car to move, and what direction
             to move it.
            3. Move car according to user's input. If movement failed
            the respective message will be printed, return False.
            4. Report to the user result of current round by printing the board
        """
        color_input = self.get_color_input()
        direction_input = gh.get_direction()
        move_validity = board.move(board.get_cars_dict()[color_input],
                                   direction_input)
        if not move_validity:
            return False
        else:
            print(board)
            return True

    def get_color_input(self):
        """
        Method requesting the color from the user for car moving
        :return: String representing the color of the car
        that user want to move
        """
        cur_car_colors_lst = \
            [color for color, car in board.get_cars_dict().items() if car]
        # create the list of colors that are available, i.e.
        # for current existing cars
        input_col = input(self.ASK_CAR_COL_MSG)
        while input_col not in cur_car_colors_lst:
            print(gh.ERROR_CAR_COLOR)
            input_col = input(self.ASK_CAR_COL_MSG)
        return input_col

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        First adding the main car, then adding the other by user input.
        Finally the game begins, call single_turn until win
        :return: None
        """
        print(self.START_GAME_MSG)
        num_cars = gh.get_num_cars()
        board.place_main_car_on_board()
        print(board)
        while num_cars != 0:
            is_given_car_parameters = board.place_cars_on_board()
            if is_given_car_parameters:
                print(board.ADD_CAR_SUCCESS_MSG)
                print(board)  # after adding the car represent the board
                num_cars -= 1
        while not board.main_car_got_exit():
            cur_turn = self.single_turn()
            while not cur_turn:
                cur_turn = self.single_turn()
        gh.report_game_over()

if __name__ == "__main__":
    """
    The main block of the code that runs the game after creating empty 
    dictionary of cars, and then creating the board for the game.
    """
    cars_dict = dict.fromkeys(gh.VALID_COLORS)
    board = Board(cars_dict, [3, 5]) # here first coord is axis_x - horizontal
    # the second one is axis_y - vertical, (0, 0) - upper left coordinate
    # *order is changed from what was given in exercise for the visual comfort
    game = Game(board)
    game.play()
