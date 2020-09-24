from hangman_helper import*

DELIMITER = ''
CHAR_A = 97
LEN_ALPHABET = 26
LEN_VALID_INPUT = 1  # declare the length of valid input - 1
ADDITIONAL_FEE = 0
A_PARAM = 0
B_PARAM = 1

def run_single_game(words_list):
    clue_word = get_random_word(words_list)  # declaration of the word for single game
    cur_pattern = '_' * len(clue_word)  # creating the string of underlines by length of the word - beginning pattern
    error_count = ADDITIONAL_FEE
    error_count_lst = []
    cur_msg = DEFAULT_MSG
    while (cur_pattern != clue_word) and (error_count < MAX_ERRORS):
        display_state(cur_pattern, error_count, error_count_lst, cur_msg)  # fixing current properties
        cur_input = get_input()
        if cur_input[B_PARAM] == None:  # check if player wants to get hint
            filtered_lst = filter_words_list(words_list, cur_pattern, error_count_lst)
            hint_letter = choose_letter(filtered_lst, cur_pattern)
            cur_msg = HINT_MSG + hint_letter
            continue  # if user asks hint we need to print the hint_letter, start new loop and wait for new input
        cur_letter = cur_input[B_PARAM]  # declaration the string that was input
        if not check_input(cur_letter):  # check if the input string is valid
            cur_msg = NON_VALID_MSG
        elif (cur_letter in error_count_lst) or (cur_letter in cur_pattern): # check if user've already made such choice
            cur_msg = ALREADY_CHOSEN_MSG + cur_letter
        elif (cur_letter in error_count_lst) or (cur_letter in cur_pattern): # check if user've already made such choice
            cur_msg = ALREADY_CHOSEN_MSG + cur_letter
        elif cur_letter not in clue_word:  # the user makes error, add one more error, and add letter to list errors
            error_count += 1
            error_count_lst.append(cur_letter)
            cur_msg = DEFAULT_MSG
        else:
            cur_pattern = update_word_pattern(clue_word, cur_pattern, cur_letter) # we are in the case when user guessed
            cur_msg = DEFAULT_MSG
    if cur_pattern == clue_word:  # the case of win
        display_state(cur_pattern, error_count, error_count_lst, WIN_MSG, True)
    elif error_count == MAX_ERRORS:  # the case of loss
        display_state(cur_pattern, error_count, error_count_lst, LOSS_MSG + clue_word, True)

def filter_words_list(words, pattern, wrong_guess_lst):
    """
    Function activates three filtres in the next order:
    1)filter on the length - nice_len_words_lst
    2)filter that excludes the words with letters that are in error list - exclude_wrong_letters
    3)filter that find the words that satisfy the current pattern - pattern_concord_words_lst
    :param words: list of words for filtering
    :param pattern: the current parrent that we concording the words for
    :param wrong_guess_lst: list of letters that are 100% not in the closed letters of the pattern
    :return: the list of filtred words
    """
    filtered_lst = nice_len_words_lst(words, pattern)
    filtered_lst = exclude_wrong_letters(filtered_lst, wrong_guess_lst)
    filtered_lst = pattern_concord_words_lst(filtered_lst, pattern)
    return filtered_lst

def nice_len_words_lst(words_lst, pattern):
    """
    the function creates list of the words from words_lst that are the same length as pattern
    :param words_lst: list of words for filtering them
    :param pattern: pattern of the word that we'll comparing with
    :return: list of words that their length is like pattern's length
    """
    nice_len_words_lst = []
    for i in range(len(words_lst)):
        if len(pattern) == len(words_lst[i]):
            nice_len_words_lst.append(words_lst[i])
    return nice_len_words_lst

def exclude_wrong_letters(words_lst, wrong_let_lst):
    """
    The function filtres the list of words by excluding the words that contain error letters
    :param words_lst: list of words for filtering
    :param wrong_let_lst: list of letters that are wrong
    :return: the new, filtered, list of words
    """
    exclude_let_lst = []
    for i in range(len(words_lst)):  # run on all words that are in the list now
        if len(wrong_let_lst) == 0:  # we have to check if the wrong_let_lst is empty, this function is unnecessary
            return words_lst
        for j in range(len(wrong_let_lst)):  # run on all letters that shouldn't appear in the words of filtered list
            if wrong_let_lst[j] in words_lst[i]:  # if the wrong letter is in the word, exclude this word (not include)
                break
            elif j == len(wrong_let_lst) - 1:  # if we've got to the last "wrong" letter and nobody of them is in the
                                            # word, need to add it
                exclude_let_lst.append(words_lst[i])
    return exclude_let_lst

def pattern_concord_words_lst(words_lst, pattern):
    """
    The function filtres the list of words by concording them to the pattern
    :param words_lst: list of words for filtering
    :param pattern: string - the pattern of symbols that we're concording to
    :return: the new, filtered, list of words
    """
    nice_pat_words_lst = []
    for i in range(len(words_lst)):  # run on all words that are in current list
        for j in range(len(pattern)):  # run on letters of pattern that already discovered
            if pattern[j] != '_' and words_lst[i][j] != pattern[j]:  # the letter from the pattern is not in word
                break
            if pattern.count(pattern[j]) < words_lst[i].count(pattern[j]):  # check that number of discovered letters
                                                                    # in the pattern is not bigger than in current word
                break
            if j == len(pattern) - 1:  # if we've got to the end of the pattern without break, current word satisfies
                nice_pat_words_lst.append(words_lst[i])
    return nice_pat_words_lst

def choose_letter(words, pattern):
    """
    The function finds the most frequent letter ,that is not in the current pattern, in list of words
    :param words: list of words
    :param pattern: string - current pattern of the game
    :return: letter that is the most possible for hint (the most frequent one)
    """
    max_quantity_let = ADDITIONAL_FEE
    cur_quantity = ADDITIONAL_FEE
    hint_let = DELIMITER
    for i in range(LEN_ALPHABET):
        if index_to_letter(i) in pattern:
            continue
        for j in range(len(words)):
            if index_to_letter(i) in words[j]:
                cur_quantity += words[j].count(index_to_letter(i))
        if cur_quantity > max_quantity_let:
            max_quantity_let = cur_quantity
            hint_let = index_to_letter(i)
        cur_quantity = ADDITIONAL_FEE
    return hint_let

def update_word_pattern(word, pattern, letter):
    """
    Function updates the word in case if the player guessed the letter right
    :param word: the whole word
    :param pattern: the current pattern with divined letters
    :param letter: letter for check
    :return: updated word pattern
    """
    pattern_lst = list(pattern)  # put the pattern symbols into list of symbols
    pattern_new = DELIMITER
    for i in range(len(word)):
        if word[i] == letter:
            pattern_lst[i] = letter
        pattern_new += pattern_lst[i]  # append the letter to the new pattern
    return pattern_new

def check_input(input_str):
    """
    Function checks if the player`s input is valid or not
    :param input: player`s input
    :return: True if player`s input is lowercase letter of latin alphabet
            False whatever
    """
    if len(input_str) != LEN_VALID_INPUT:  # check the length of the symbol
        return False
    for i in range(LEN_ALPHABET):
        if index_to_letter(i) == input_str:  # check possession of symbol to the lowercase latin alphabet
            return True
    return False

def index_to_letter(index):
    """Return the letter corresponding to the given index"""
    return chr(index + CHAR_A)

def main():
    run_single_game(load_words())
    while get_input()[B_PARAM] != False:  # the game will be finished only if the user pushes button 'No More!'
        run_single_game(load_words())

if __name__=="__main__":
    start_gui_and_call_main(main)
    close_gui()