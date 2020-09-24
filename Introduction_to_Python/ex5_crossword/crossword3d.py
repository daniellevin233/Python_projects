####################################
# FILE : crossword3d.py
# WRITERS : daniel_levin , daniellevin , 336462874
#           itzik_foichtvanger , itzikf100, 203208798
# EXERCISE : intro2cs ex5 2017-2018
# DESCRIPTION : The programme that works with input files and counts appearances of the words from word_list file in
# three dimensional crossword from the mat file in addition to directions that were input as the forth parameter.
# The code activating will create file from type txt, in the current folder in the case of all arguments valid.
####################################
from crossword import*

DEPTH_DIR = 'a'
LENGTH_DIR = 'b'
WIDTH_DIR = 'c'
LST_3D_DIR = [DEPTH_DIR, LENGTH_DIR, WIDTH_DIR]

def run_crossword_3d(words_lst_path, mat_3d_path, output_path, dir_3d_str):
    """
    The basis function that calls to function for processing the input files and then to function that creates the new
    file with wanted parameters
    :param words_lst_path: Path to file with words that we want to search and count
    :param mat_3d_path: Path to file with three dimensional matrix that we will search in
    :param output_path: Path of the file that we will put the results into
    :param dir_3d_str: The string of directions for searching
    :return: As a result of calling to function will be created file with counted words in addition to directions
    """
    counted_words_lst, output_dir = work_with_files_3d(words_lst_path, mat_3d_path, dir_3d_str)
    create_output_file(counted_words_lst, output_path, output_dir)

def work_with_files_3d(words_path, mat_3d_path, dir_3d_str):
    """
    Function processes the files. Checking the validity of given files pathes. Opening the files, working with them
    in functions (see explanation in functions).
    :param words_path: Path to file with words that we want to search and count
    :param mat_3d_path: Path to file with three dimensional matrice that we will search in
    :param dir_3d_str: The string of three dimensional directions for searching
    :return: First return is the list of strings that represent counted words, conclude: ['cat, 1', 'dog, 2'...].
            Second return is the string of valid directions without reduplication, that we've searched in
    """
    check_files_existence(words_path, mat_3d_path)
    check_dir_str(dir_3d_str, LST_3D_DIR)
    with open(words_path) as word_lst_file:
        words_lst_search = words_to_lst(word_lst_file)
    with open(mat_3d_path) as matrix_3d_file:
        words_lst_3d = blocks_to_3d_lst(matrix_3d_file)
    if words_lst_3d == [[]]:  # If the matrix file is empty we need to continue code and return empty list in the end
        wanted_matrices = []
    else:
        wanted_matrices = blocks_to_wanted_2d_matrices(words_lst_3d, dir_3d_str)  # create lst of 2d matrices
    wanted_str_lst = work_with_lst_of_3d_mat(wanted_matrices)  # refer to crossword.py to find words in 2d matrices
    counted_words_lst_3d = create_counted_words_lst(words_lst_search, wanted_str_lst)  # count the words in fixed strings
    return counted_words_lst_3d, dir_3d_str

def blocks_to_wanted_2d_matrices(words_3d_lst, directions_str):
    """
    Function changes the three dimensional list (i.e. the matrices that are inside) to matrices depth, length ot width
    in addition to given direction.
    :param words_3d_lst: Three dimensional list of matrices.
    :param directions_str: String of directions that we gonna find the words in the space.
    :return: Three dimensional list of two dimensional matrices that satisfy the condition of directions.
    """
    mat_2d_lst = []
    if DEPTH_DIR in directions_str:
        mat_2d_lst += words_3d_lst
    if LENGTH_DIR in directions_str:
        mat_2d_lst += create_length_mat_lst(words_3d_lst)
    if WIDTH_DIR in directions_str:
        mat_2d_lst += create_width_mat_lst(words_3d_lst)
    return mat_2d_lst

def create_length_mat_lst(words_3d_lst):
    """
    The function creates the list of two dimensional matrices in addition to length
    in relation to matrices that were given.
    :param words_3d_lst: The three dimensional list that represents letters of given matrices in the right order
    :return: Three dimensional list of two dimensional matrices that ordered in addition to length
    """
    new_2d_mat_lst, cur_2d_mat = [], []
    for j in range(len(words_3d_lst[FIRST_ELEMENT_INDEX])):  # we can assume that all matrices are of the same length,
        # so take the length of the first matrix
        for cur_mat in words_3d_lst:  # run onto internal 2d matrices
            cur_2d_mat.append(cur_mat[j])
        new_2d_mat_lst.append(cur_2d_mat)
        cur_2d_mat = []
    return new_2d_mat_lst

def create_width_mat_lst(words_3d_lst):
    """
    The function creates the list of two dimensional matrices in addition to width
    in relation to matrices that were given.
    :param words_3d_lst: The three dimensional list that represents letters of given matrices in the right order
    :return: Three dimensional list of two dimensional matrices that ordered in addition to width
    """
    new_2d_mat_lst, cur_2d_mat, cur_column = [], [], []  # we gonna create three dimensional list
    for i in range(len(words_3d_lst[0][0])):  # we can assume that all words in all matrices are of the same length,
        # so take the length of the first word in the first matrix
        for cur_mat in words_3d_lst:  # run onto two dimensional matrices of the list
            for cur_word in cur_mat:  # run onto words of current two dimensional matrix
                cur_2d_mat.append(cur_word[i])
            cur_column.append(cur_2d_mat)
            cur_2d_mat = []
        new_2d_mat_lst.append(cur_column)
        cur_column = []
    return new_2d_mat_lst

def work_with_lst_of_3d_mat(matrices_2d_lst):
    """
    Function runs on two dimensional matrices of three dimensional list that satisfy us on this point, and find strings
    in directions from constant DIR_2D. The process is to call to function "matrix_to_wanted_strings" from crossword.py
    :param matrices_2d_lst: List of two dimensional matrices
    :return: List of strings that satisfy us for given matrices
    """
    wanted_strings_lst = []
    for cur_mat in matrices_2d_lst:
        wanted_strings_lst += matrix_to_wanted_strings(cur_mat, DIRECTIONS_2D)
    return wanted_strings_lst

def blocks_to_3d_lst(matrix_3d_file):
    """
    Function creates three dimensional list of letters from the file that was given as a parameter.
    :param matrix_3d_file: File that contains words in shape of three dimensional
    :return: Three dimensional list, external list contains separated matrices, the first internal list contains strings
    in addition to lines, and last internal lists contain letters of current line
    """
    letters_lst_mat, mat_3d_lst = [], []
    for line in matrix_3d_file:
        if line == '***\n':  # the matrix ends on strings like "***\n"
            mat_3d_lst.append(letters_lst_mat)
            letters_lst_mat = []
            continue
        letters_lst_mat.append(line_to_lst(line))
    else:  # if we've got to the end of the file we need to append the last matrix and finish the function
        mat_3d_lst.append(letters_lst_mat)
    return mat_3d_lst

if __name__ == '__main__':
    """
    The condition for activating the programme. Calling to run_crossword function with given from terminal arguments 
    """
    if len(sys.argv) == NUMBER_OF_ARGUMENTS + 1:  # check the validity of given argument number
        run_crossword_3d(sys.argv[WORDS_ARG], sys.argv[MATRIX_ARG], sys.argv[OUTPUT_ARG], sys.argv[DIRECTIONS_ARG])
    else:  # the number of given arguments is false, so print error message
        print(ERROR_MSG)