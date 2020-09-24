####################################
# FILE : crossword.py
# WRITERS : daniel_levin , daniellevin , 336462874
#           itzik_foichtvanger , itzikf100, 203208798
# EXERCISE : intro2cs ex5 2017-2018
# DESCRIPTION : The programme that works with input files and counts appearances of the words from word_list file in
# two dimensional crossword from the mat file in addition to directions that were input as the forth parameter.
# The code activating will create file from type txt, in the current folder in the case of all arguments valid.
####################################
import sys
import os

NUMBER_OF_ARGUMENTS = 4
ERROR_MSG = "ERROR: invalid number of parameters. Please enter word_file matrix_file output_file directions."
INVALID_ERROR_MSG = "ERROR: invalid directions."
WORDS_LST_EXIST_ERROR_MSG = "ERROR: Word file word_list.txt does not exist."
MAT_EXIST_ERROR_MSG = "ERROR: Matrix file mat.txt does not exist."
DELIMITER = ''
WORDS_ARG = 1
MATRIX_ARG = 2
OUTPUT_ARG = 3
DIRECTIONS_ARG = 4
EMPTY_LST_LENGTH = 0
FIRST_ELEMENT_INDEX = 0
DEFAULT_COUNTER_INDEX = 0

UP_DIR = 'u'
DOWN_DIR = 'd'
RIGHT_DIR = 'r'
LEFT_DIR = 'l'
RIGHT_UP_DIR = 'w'
LEFT_UP_DIR = 'x'
RIGHT_DOWN_DIR = 'y'
LEFT_DOWN_DIR = 'z'
# This 8 constants sign the direction of finding the words in matrix
DIRECTIONS_2D = UP_DIR + DOWN_DIR + RIGHT_DIR + LEFT_DIR + RIGHT_UP_DIR + LEFT_UP_DIR + RIGHT_DOWN_DIR + LEFT_DOWN_DIR
# The string of all existing directions for two dimensional matrix

def run_crossword(words_lst_path, matrix_path, output_path, directions_str):
    """
    The basis function that calls to function for processing the input files and then to function that creates the new
    file with wanted parameters
    :param words_lst_path: Path to file with words that we want to search and count
    :param matrix_path: Path to file with two dimensional matrix that we will search in
    :param output_path: Path of the file that we will put the results into
    :param directions_str: The string of directions for searching
    :return: As a result of calling to function will be created file with counted words in addition to directions
    """
    counted_words_lst, output_dir_str = work_with_files(words_lst_path, matrix_path, directions_str)
    create_output_file(counted_words_lst, output_path, output_dir_str)

def work_with_files(words_path, mat_path, dir_str):
    """
    Function processes the files. Checking the validity of given files pathes. Opening the files, working with them
    in functions (see explanation in functions).
    :param words_path: Path to file with words that we want to search and count
    :param mat_path: Path to file with two dimensional matrice that we will search in
    :param dir_str: The string of two dimensional directions for searching
    :return: First return is the list of strings that represent counted words, conclude: ['cat, 1', 'dog, 2'...].
            Second return is the string of valid directions without reduplication, that we've searched in
    """
    check_files_existence(words_path, mat_path)
    check_dir_str(dir_str)
    with open(words_path) as word_lst_file:
        words_lst_search = words_to_lst(word_lst_file)
    with open(mat_path) as matrix_file:
        words_lst_2d = matrix_to_words(matrix_file)
    if words_lst_2d == []:  # If the matrix file is empty we need to continue code and return empty list in the end
        wanted_strings = []
    else:
        wanted_strings = matrix_to_wanted_strings(words_lst_2d, dir_str)  # Else matrix --> to wanted strings
    counted_words_lst = create_counted_words_lst(words_lst_search, wanted_strings)  # create list of counted words
    return counted_words_lst, dir_str

def check_files_existence(words_path, matrix_path):
    """
    Function checks the files existence, in case if file doesn't exist will be printed the error message and running
    the programme will finish
    :param words_path: Path to file with words that we want to search and count
    :param matrix_path: Path to file with two dimensional matrix that we will search in
    :return: Finishing the programme in case of not existing, None elsewhere
    """
    if os.path.exists(words_path) and os.path.exists(matrix_path):
        return None
    if not os.path.exists(words_path):
        print(WORDS_LST_EXIST_ERROR_MSG)
    else:
        print(MAT_EXIST_ERROR_MSG)
    return sys.exit()

def words_to_lst(words_txt):
    """
    Function works with file of words, and creates the list of strings (words) that are in file
    :param words_txt: The file with words
    :return: List of words from file in alphabetical order
    """
    lst = []
    for line in words_txt:
        lst.append(line.strip().lower())  # we need to find also uppercase letters, so put all in lowercase
    nice_lst = sorted(lst)  # sort the words in order alphabet to get the output in order alphabet
    return nice_lst

def matrix_to_words(mat_txt):
    """
    Function creates the two dimensional list that represents letters in the matrix
    :param mat_txt: The file that contains the crossword letters, divided by commas, the strings divided by '\n'.
    :return: Two dimensional list, each internal list contains strings - letters
    """
    letters_lst_2d = []
    for line in mat_txt:
        letters_lst_2d.append(line_to_lst(line))
    return letters_lst_2d

def line_to_lst(string):
    """
    Function delete all the commas from the string and creates list of letters that are in the string
    :param string: string of letters divided by commas
    :return: List of letters of the given string
    """
    return string.strip().lower().split(',')  # We want to work with uppercase too, that's why make lower().

def check_dir_str(dir_string, dir_str=DIRECTIONS_2D):
    """
    Function "checks the validity of input file directions" and if at least one symbol is not valid error message will
    be printed and the programme will be finished
    :param dir_string: String with directions for searching
    :return:In the case of validity of all the symbols in the directions string that was input: None
    In the case of invalidity of at least one symbol in the string: Finishing the programme
    """
    for i in range(len(dir_string)):
        if dir_string[i] not in dir_str:  # at least one symbol isn't from DIRECTIONS_2D print err_msg and stop the code
            print(INVALID_ERROR_MSG)
            return sys.exit()
    return None

def matrix_to_wanted_strings(lst_2d, directions_str):
    """
    This function calls to another functions depending on which direction was got for checking words in the matrix
    :param lst_2d: Two dimensional list of letters of crossword
    :param directions_str: String that was got from command, it contains the letters signing the direction for searching
    :return: List of strings that are interesting for us, i.e. if for example was given command for looking the lines
    from top to down, function will return list of strings that are set of all columns in direction from top to down.
    So on for all directions that appear in the directions_str. In the case of several directions given, all strings
    will be appear into one list.
    """
    lst_of_str = []
    if DOWN_DIR in directions_str:
        lst_of_str += matrix_to_columns(lst_2d)
    if UP_DIR in directions_str:
        lst_of_str += reverse_strings_of_lst(matrix_to_columns(lst_2d))
    if RIGHT_DIR in directions_str:
        lst_of_str += matrix_to_lines(lst_2d)
    if LEFT_DIR in directions_str:
        lst_of_str += reverse_strings_of_lst(matrix_to_lines(lst_2d))
    if RIGHT_DOWN_DIR in directions_str:
        lst_of_str += matrix_to_main_diag(lst_2d)
    if LEFT_UP_DIR in directions_str:
        lst_of_str += reverse_strings_of_lst(matrix_to_main_diag(lst_2d))
    if LEFT_DOWN_DIR in directions_str:
        lst_of_str += matrix_to_minor_diag(lst_2d)
    if RIGHT_UP_DIR in directions_str:
        lst_of_str += reverse_strings_of_lst(matrix_to_minor_diag(lst_2d))
    return lst_of_str

def matrix_to_lines(lst_2d):
    """
    Function will create list of strings that sign the corresponding lefttoright lines in crossword
    :param lst_2d: Two dimensional list of letters that sign the matrix.
    :return: List of strings that sign lines in coherent direction
    """
    lst_of_lines = []
    for internal_lst in lst_2d:
        str_line = DELIMITER
        for cur_let in internal_lst:
            str_line += cur_let
        lst_of_lines.append(str_line)
    return lst_of_lines

def matrix_to_columns(lst_2d):
    """
    Function will create list of strings that sign the corresponding toptodown columns in crossword
    :param lst_2d: Two dimensional list of letters that sign the matrix.
    :return: List of strings that sign columns in coherent direction
    """
    lst_of_columns = []
    for i in range(len(lst_2d[FIRST_ELEMENT_INDEX])):  # we run in range of quantity of columns
        str_column = DELIMITER
        for j in range(len(lst_2d)):
            str_column += lst_2d[j][i]
        lst_of_columns.append(str_column)
    return lst_of_columns

def matrix_to_main_diag(lst_2d):
    """
    Function will create list of strings that sign the corresponding main diagonal
    and all other diagonal that parallel to main in crossword.
    The process is calling to two functions for main diagonals
    Read more here about main diagonal: https://en.wikipedia.org/wiki/Main_diagonal
    :param lst_2d: Two dimensional list of letters that sign the matrix.
    :return: List of strings that sign diagonals in coherent direction
    """
    lst_of_main_diag_str = first_column_diag(lst_2d) + first_row_main_diag(lst_2d)
    return lst_of_main_diag_str

def first_column_diag(lst_2d):
    """
    Function will create list of strings that sign the corresponding main diagonal that begins on first column
    and all other diagonal that begins on first column in crossword.
    :param lst_2d: Two dimensional list of letters that sign the matrix.
    :return: List of strings that sign coherent diagonals
    """
    lst_of_first_col_diag_str = []
    for i in range(len(lst_2d)):
        str_main_diag = DELIMITER
        index_i = i  # we need here the internal index because we increase either string index either column index
        for j in range(len(lst_2d[FIRST_ELEMENT_INDEX])):
            str_main_diag += lst_2d[index_i][j]
            if index_i + 1 == len(lst_2d) or j + 1 == len(lst_2d[FIRST_ELEMENT_INDEX]):  # check if we've got to border
                lst_of_first_col_diag_str.append(str_main_diag)
                break
            index_i += 1
    return lst_of_first_col_diag_str

def first_row_main_diag(lst_2d):
    """
    Function will create list of strings that sign the corresponding main diagonal that begins on first row of matrix
    and all other diagonal that begins on first row in crossword.
    :param lst_2d: Two dimensional list of letters that sign the matrix.
    :return: List of strings that sign coherent diagonals
    """
    lst_of_first_row_diag_str = []
    for j in range(FIRST_ELEMENT_INDEX + 1, len(lst_2d[FIRST_ELEMENT_INDEX])):  # begin from (FIRST_ELEMENT_INDEX + 1)
        # because we've already add the longest main diagonal
        str_main_diag = DELIMITER
        index_j = j  # again use the internal index that begins from the external one
        for i in range(len(lst_2d)):
            str_main_diag += lst_2d[i][index_j]
            if index_j + 1 == len(lst_2d[FIRST_ELEMENT_INDEX]) or i + 1 == len(lst_2d):  #check if we've got to border
                lst_of_first_row_diag_str.append(str_main_diag)
                break
            index_j += 1
    return lst_of_first_row_diag_str

def matrix_to_minor_diag(lst_2d):
    """
    Function will create list of strings that sign the corresponding minor diagonal
    and all other diagonal that parallel to minor in crossword.
    The process is calling to two functions for minor diagonals
    :param lst_2d: Two dimensional list of letters that sign the matrix.
    :return: List of strings that signs diagonals in coherent direction
    """
    lst_of_minor_diag_str = last_column_diag(lst_2d) + first_row_minor_diag(lst_2d)
    return lst_of_minor_diag_str

def last_column_diag(lst_2d):
    """
    Function will create list of strings that sign the corresponding minor diagonal that begins on last column of matrix
    and all other diagonal that begins on last column in crossword.
    :param lst_2d: Two dimensional list of letters that sign the matrix.
    :return: List of strings that sign coherent diagonals
    """
    lst_of_last_col_diag_str = []
    for i in range(len(lst_2d)):
        str_minor_diag = DELIMITER
        index_i = i  # internal index begins from internal one, it signs columns here
        for j in range(len(lst_2d[FIRST_ELEMENT_INDEX]) - 1, -1, -1):  # we run from the edge to the beginning
            str_minor_diag += lst_2d[index_i][j]
            if index_i + 1  == len(lst_2d) or j == FIRST_ELEMENT_INDEX:  # check if've got to border
                lst_of_last_col_diag_str.append(str_minor_diag)
                break
            index_i += 1
    return lst_of_last_col_diag_str

def first_row_minor_diag(lst_2d):
    """
    Function will create list of strings that sign the corresponding minor diagonal that begins on first row of matrix
    and all other diagonal that begins on first row in crossword.
    :param lst_2d: Two dimensional list of letters that sign the matrix.
    :return: List of strings that sign coherent diagonals
    """
    lst_of_first_row_minor_diag_str = []
    for j in range(len(lst_2d[FIRST_ELEMENT_INDEX]) - 2, -1, -1):  # again we run from the edge to the beginning
        # begin from (lst_2d[FIRST_ELEMENT_INDEX]) - 2) because we've already add the longest minor diagonal
        str_minor_diag = DELIMITER
        index_j = j  # internal index that begins from external one, it signs columns
        for i in range(len(lst_2d)):
            str_minor_diag += lst_2d[i][index_j]
            if index_j == FIRST_ELEMENT_INDEX or i + 1 == len(lst_2d):  # check the border
                lst_of_first_row_minor_diag_str.append(str_minor_diag)
                break
            index_j -= 1
    return lst_of_first_row_minor_diag_str

def reverse_strings_of_lst(lst_of_strings):
    """
    Function reverses all the strings of given two dimensional list
    :param lst_of_strings: List of strings
    :return: List of strings that are reversed
    """
    lst_of_reversed_str = [x[::-1] for x in lst_of_strings]
    return lst_of_reversed_str

def create_counted_words_lst(words_lst, strings_lst):
    """
    Function creates the list of strings that contain the word from words_lst if the word appears in the strings of
    strings_lst, comma, and quantity of appearances.
    :param words_lst: The words for searching
    :param strings_lst: The list of strings that we are looking in
    :return: The list of strings where each one contains counted word
    """
    counted_lst = []
    for word in words_lst:
        cur_word_counter = DEFAULT_COUNTER_INDEX
        for cur_str in strings_lst:
            cur_word_counter += count_word_in_string(word, cur_str)
        if cur_word_counter != DEFAULT_COUNTER_INDEX:
            counted_lst.append(word + ',' + str(cur_word_counter))
    return counted_lst

def count_word_in_string(word, string):
    """
    Function counts how much times word appears in string. For parameters ('pop','popop') function returns 2.
    :param word: String that we are interested to count
    :param string: String that we are counting in
    :return: Integer number - times that word appears in string
    """
    word_in_string_counter = DEFAULT_COUNTER_INDEX  # sign the starting value of counter
    if len(word) > len(string) or word not in string:  # get off the case when we don't need to check anything
        return word_in_string_counter
    for start_index in range(len(string)):
        if word == string[start_index:(start_index + len(word))]:  # check the word from the current index to it length
            word_in_string_counter += 1
    return word_in_string_counter

def create_output_file(output_lst, outfile_path, dir_str):
    """
    The function creates the file in current folder
    :param output_lst: The list of words that we need to write in new file
    :param outfile_path: The path of file that we need write into
    :param dir_str: The string of directions that we searched for them
    :return: New file will be created in the current folder
    """
    if os.path.exists(outfile_path):  # the file exists so destroy what it contains and write there
        with open(outfile_path, 'w') as output_file:
            write_lst_to_outfile(output_file, output_lst)
    else:  # the file doesn't exist so create the new file
        with open('outfile_' + dir_str + '.txt', 'w') as output_file:  # create name of file: outfile_ plus directions
            write_lst_to_outfile(output_file, output_lst)

def write_lst_to_outfile(file, lst):
    """
    Function writes the strings of the list to file
    :param file: The address of the file that we need to write in
    :param lst: List of strings that we need to add to the file
    """
    if len(lst) != EMPTY_LST_LENGTH:
        for line in lst[:-1]:  # We do passing line (enter - "\n") for all lines except the last one
            file.write(line + '\n')
        file.write(lst[-1])  # The last line we write without passing to the new line
    else:  # if we got the empty lst we still need to create empty file
        file.write(DELIMITER)

if __name__ == '__main__':
    """
    The condition for activating the programme. Calling to run_crossword function with given from terminal arguments 
    """
    if len(sys.argv) == NUMBER_OF_ARGUMENTS + 1:  # check the validity of given argument number
        run_crossword(sys.argv[WORDS_ARG], sys.argv[MATRIX_ARG], sys.argv[OUTPUT_ARG], sys.argv[DIRECTIONS_ARG])
    else:  # the number of given arguments is false, so print error message
        print(ERROR_MSG)