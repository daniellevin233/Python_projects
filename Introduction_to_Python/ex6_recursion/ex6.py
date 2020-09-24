#############################################################
# FILE : ex6.py
# WRITER : Daniel Levin , daniellevin , 336462874
# EXERCISE : intro2cs ex6 2017-2018
# DESCRIPTION: Recursive functions for solving different mathematical problems and game hanoi
#############################################################

DELIMITER = ''

def print_to_n(n):
    """
    The function prints integer numbers from 1 to n by recursive calling to itself.
    :param n: number n
    """
    if n <= 0:
        return
    if n == 1:  # the basic case
        print(n)
    else:
        print_to_n(n - 1), print(n)

def print_reversed(n):
    """
    The function prints integer numbers from n to 1 by recursive calling to itself.
    :param n: number n
    """
    if n <= 0:
        return
    if n == 1:  # the basic case
        print(n)
    else:
        print(n), print_reversed(n - 1)

def has_divisor_smaller_than(n, i):
    """
    Function checks if exist divisors of number n between 1 and i. Function works recursively. On each recursive call
    function checks if current value of i divides the n, and if yes, one of the boolean values in the conjunction
    will be False, so False will be returned.
    :param n: Natural number that we are searching divisors for.
    :param i: Integer number smaller than n, we are searching divisors for n that are below i.
    :return: True if exist divisors of n between 1 and i, false if they don't exist. (1 is not divisor)
    """
    if i == 1:  # the base case
        return True
    if n % i == 0 and i < n:  # we've got divisor of n that is smaller than n
        return False
    else:
        return has_divisor_smaller_than(n, i - 1) and True  # if at least one number below i divide n, we'll get False

def is_prime(n):
    """
    Function checks whether the number n prime or not by calling to recursive function has_divisor_smaller_than.
    Enough to check divisors below n//2 because all of them are not bigger than n/2.
    :param n: number n
    :return: True if n is prime, False otherwise
    """
    if n <= 1:  # 1, 0 and negative are not prime numbers
        return False
    else:
        return has_divisor_smaller_than(n, n//2)  # if n has divisors they are not bigger than n//2

def divisors(n):
    """
    Function creates list of divisors of integer number n by calling to recursive function create_divisors_lst.
    If n is negative, still will be returned positive divisors.
    :param n: number n
    :return: list of divisors of n
    """
    divisors_lst = []
    if n == 0:  # print empty list
        return divisors_lst
    else:
        return create_divisors_lst(abs(n), divisors_lst)  # positive divisors of the number and
        # its absolute value are the same

def create_divisors_lst(n, div_lst, i=1):
    """
    Function creates list of divisors of number n between 1 and n//2 + 1, and puts it into div_lst by recursive calling
    to itself with increasing i by 1
    :param n: number n that is positive and not 0
    :param div_lst: list that we are puting divisors in
    :param i: the default value of function that gives possibility to work recursively
    :return: List of n's divisors
    """
    if i == n//2 + 1:  # the basic case
        return div_lst + [n]  # we've got to the n//2+1 so need to add n to the list because n always divides n
    if n % i == 0:
        div_lst.append(i) # here i divides n
    return create_divisors_lst(n, div_lst, i + 1)

def factorial(n):
    """
    Function counts the factorial of the number n by recursive calling ot itself
    :param n: number n
    :return: factorial of n
    """
    if n == 0:  # the base case
        return 1
    return n*factorial(n - 1)

def degree(x, i):
    """
    Function counts the value of x in degree i by recursive calling to itself
    :param x: number that we are rising in degree
    :param i: the degree that we are rising in
    :return: x^i
    """
    if i == 0:  # the base case
        return 1
    if i == 1:
        return x
    return x*degree(x, i - 1)

def exp_n_x(n, x):
    """
    Function counts the value of EXPn(x) be recursive calling to itself
    :param n: number n
    :param x: point that we are counting in
    :return: value of sum of (x^i)/n! for 0 <= i <= n - the exponent value
    """
    if n == 0:  # base case
        return degree(x, n)/factorial(n)
    return degree(x, n)/factorial(n) + exp_n_x(n - 1, x)

def play_hanoi(hanoi, n, src, dest, tmp):
    """
    Function uses the file hanoi_game.py to realise shifting n disks from column src to column dest, keeping their order
    Recursive calling: moving n-1 disks from src to tmp, then moving 1 remaining disk to dest, it is the biggest
    and than again moving n-1 disks from tmp to dest on the top of the biggest one
    :param hanoi: interface of the game
    :param n: quantity of disks
    :param src: the first column that contains all the disks on the beginning of the game
    :param dest: the destination column that we are shifting disks on
    :param tmp: the third column that we are using to move disks
    """
    if n <= 0:  # the basic case
        return
    return play_hanoi(hanoi, n - 1, src, tmp, dest), hanoi.move(src, dest), play_hanoi(hanoi, n - 1, tmp, dest, src)

def print_binary_sequences(n):
    """
    Function prints all possible sequences by length n of 0 and 1,
    by calling to recursive function print_sequences_with_prefix
    :param n: length of sequences
    """
    binary_lst = ['0', '1']  # declare the list of necessary numbers
    if n == 0:  # the sequences by length 0 are empty strings
        print(DELIMITER)
    else:
        for char in binary_lst:
            print_sequences_with_prefix(char, binary_lst, n)

def print_sequences(char_list, n):
    """
    Function prints all possible sequences by length n of characters from char_list,
    by calling to recursive function print_sequences_with_prefix
    :param char_list: list of characters that will appear in the sequences
    :param n: length of sequences
    """
    if n == 0:  # the sequences by length 0 are empty strings
        print(DELIMITER)
    else:
        for char in char_list:
            print_sequences_with_prefix(char, char_list, n)

def print_sequences_with_prefix(prefix, char_list, n):
    """
    Function prints all possible sequences of strings that begin on prefix and contain chars from char_list
    by recursive calling to itself with diminishing n by 1
    :param prefix: The string that all sequences begin with it.
    :param char_list: List of characters that will appear in sequences.
    :param n: Length of sequences.
    """
    if n == 1:  # the basic case
        print(prefix)
    else:
        for new_char in char_list:
            print_sequences_with_prefix(prefix + new_char, char_list, n - 1)

def print_no_repetition_sequences(char_list, n):
    """
    Function prints all possible sequences by length n of characters
    from char_list without repetitions, by calling to recursive function print_sequences_with_prefix.
    :param char_list: list of characters that will appear in the sequences
    :param n: length of sequences
    """
    if n == 0:
        print(DELIMITER)
    else:
        for char in char_list:
            print_no_repetition_sequences_with_prefix(char, char_list, n)

def print_no_repetition_sequences_with_prefix(prefix, char_list, n):
    """
    Function prints all possible sequences of strings that begin on prefix
    and contain chars from char_list without repetitions by recursive calling
    to itself by diminishing n by 1.
    :param prefix: The string that all sequences begin with it.
    :param char_list: List of characters that will appear in sequences.
    :param n: Length of sequences.
    """
    if n == 1:  # the basic case
        print(prefix)
    else:
        no_repetition_char_list = [char for char in char_list if char not in prefix]  # new list of different chars
        for new_char in no_repetition_char_list:
            print_no_repetition_sequences_with_prefix(prefix + new_char, no_repetition_char_list, n - 1)

def no_repetition_sequences_list(char_list, n):
    """
    Function creates list of strings  of all possible sequences by length n of characters
    from char_list without repetitions, by calling to recursive
    function no_repetition_sequences_with_prefix_lst.
    :param char_list: list of characters that will appear in the sequences
    :param n: length of sequences
    :return: List with possible sequences without repetitions
    """
    sequences_lst = []
    if n == 0:  # return list that contains empty string ''
        sequences_lst.append(DELIMITER)
    else:
        for char in char_list:
            sequences_lst = no_repetition_sequences_with_prefix_lst(char, char_list, n)
    return sequences_lst

def no_repetition_sequences_with_prefix_lst(prefix, char_list, n, seq_lst=[]):
    """
    Function creates list of strings of all possible sequences of strings that begin on prefix
    and contain chars from char_list without repetitions by recursive calling
    to itself by diminishing n by 1.
    :param prefix: The string that all sequences begin with it.
    :param char_list: List of characters that will appear in sequences.
    :param n: Length of sequences.
    :param seq_lst: defaultive value - empty list that we are adding to
    :return: List with possible sequences without repetitions that begin on prefix
    """
    if n == 1:  # the basic case
        seq_lst.append(prefix)
    else:
        no_repetition_char_list = [char for char in char_list if char not in prefix]  # list with different characters
        for new_char in no_repetition_char_list:
            no_repetition_sequences_with_prefix_lst(prefix + new_char, char_list, n - 1, seq_lst)
    return seq_lst
