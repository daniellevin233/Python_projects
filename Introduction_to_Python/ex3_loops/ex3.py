import math
MIN_PRIME_NUM = 2  # minimal prime number

def create_list():
    """The function returns the list of inputed by user string"""
    user_list = []
    user_input = None  # declaration of defaultive "empty" value for string that user is going to input
    while user_input != '':
        user_input = input()  # waiting for user's inputs
        if user_input != '':  # condition for NOT appending the empty string in the end of list
            user_list.append(user_input)
    return user_list

def concat_list(str_list):
    """
    This function unites the strings from the str_list given as a parameter into one string
    :param str_list: the list of strings
    :return: the union of the strings of the list in one string
    """
    sum_string = ''  # declaration of the beginning "empty" string
    for i in range(len(str_list)):  # we run on all the elements of the list that was given as parameter
        sum_string = sum_string + str_list[i]  # summing the recent string with the next in the list
    return sum_string

def average(num_list):
    """
    This function gets num_list and returns average value of them
    :param num_list: the list of numbers
    :return: None if the list is empty, in another case the average of numbers from the list
    """
    nums_quantity = 0
    sum_of_nums = 0
    if len(num_list) == 0:  # check if the given list is not empty
        return None
    for i in range(len(num_list)):  # we run on all numbers of the list
        sum_of_nums = sum_of_nums + num_list[i]  # counting their sum
        nums_quantity = nums_quantity + 1  # counting their quantity
    num_average = sum_of_nums / nums_quantity  # the formula for average value
    return num_average

def cyclic(lst1, lst2):
    """
    The function fixes if one list is the cyclic permutation of another one, or conversely
    you can read about what is cyclic permutation here: https://en.wikipedia.org/wiki/Cyclic_permutation
    Algorithm - firstly we try to find if the first element (check_elem) of lst1 included in lst2.
    If yes, we check all the next elements gradually. If something not equal we`ll try to find the next element in lst2
    that is the same as check_elem. And check all the next elements after it gradually again. And so on.
    :param lst1:the first list that contains elements of any types
    :param lst2:the second list that contains elements of any types
    :return:True if one list is cyclic petmutation of the second or conversely, False in all other cases
    """
    if len(lst1) != len(lst2):  # checking that the lists' lengths are equal
        return False
    if lst1 == lst2:  # if our lists are empty or apriori equal we can save the running time
        return True
    check_elem = lst1[0]  # variable for checking the first element of lst1
    for i in range(len(lst1)):
        if check_elem == lst2[i]:
            for j in range(1, len(lst1)):
                if lst1[j] != lst2[(i+j) % len(lst2)]:  # if we`ve got out of the lst2 we need to come back to begin
                    break
                elif j == len(lst1) - 1:  # if we`ve reached the last index in lst1 without "!=", we`ve done
                    return True
    return False

def histogram(n,num_list):
    """
    Function returns histogram of the num_list for int numbers from 0 to n-1
    read more about histogram here: https://en.wikipedia.org/wiki/Histogram#Mathematical_definition
    we assume that list_hist contains n zeros in the beginning, and then we check
    how frequent the numbers from 0 to 1 appear in the num_list, increasing the relevant element in histogram by 1
    :param n:the length of histogram, we want to check numbers from 0 to n-1
    :param num_list:the list of int numbers that we're counting frequency of (0--n-1) in
    :return:histogram on length n for numbers from num_list
    """
    list_hist = []
    for i in range(n):  # create the histogram and fill it by n zeros
        list_hist.append(0)
    for j in range(n):  # j is the int numbers from 0 to n-1 that we're looking for in num_list
        for k in range(len(num_list)):  # run on all the elements of num_list
            if num_list[k] == j:  # each time that we've found j in num_list,
                                # increase the relevant element in the list_hist by 1
                list_hist[j] = list_hist[j] + 1
    return list_hist

def prime_factors(n):
    """
    The function works in this way: we've proved in course "Discrete mathematics"
    that all prime factors of the natural number are less or equal the root of this number.
    So in the loop we run from 2 - the minimal prime number - to root of n plus 1
    (because the root itself can be prime factor of number) for example: sqrt(9)=3 and 9%3=0
    If n is prime number function returns just this number.
    The "while" works until n!=1 because if n=1 that means that we've already divided n by all its prime factors
    so we can stop to run
    :param n: integer number, we're looking for him prime factors
    :return:list of all prime factors of n
    """
    prime_num_lst = []  # the list of prime factors of n
    while n != 1:
        factor = 1
        root_n = int(math.sqrt(n))
        for i in range(MIN_PRIME_NUM, root_n + 1):  # i is candidate for the prime factor of n
            if (n % i) != 0:
                continue
            prime_num_lst.append(i)  # adding i to the list, because it's a prime factor of n on this point
            factor = i
            break  # we've found the min prime factor on this point so we can exit the loop
            # and begin it with the next number
        n = n / factor  # we divide n by its min prime factor and pass to checking the number that is result of deviding
        if factor == 1:  # if we didn't enter the upper loop, n is already prime, so let's add n into list
            prime_num_lst.append(int(n))
            break  # if there is no prime factors that less then n, n is a prime number, so we can break the "while"
    return prime_num_lst

def cartesian(lst1, lst2):
    """
    The function uses nested loops to run on the all possible pairs that satisfy the next condition:
    the first element in pair is from the first list, the second is from the second.
    :param lst1: the first list of elements
    :param lst2: the second list of elements
    :return: the cartesian product of lst1 and lst2
    """
    cart_res = []  # variable for result of cartesian product
    if (len(lst1) != 0) and (len(lst2) != 0):  # if one of the lists is empty we should return the empty list
        for i in range(len(lst1)):  # running on elements of the first list
            for j in range(len(lst2)):  # running on elements of the second list
                cart_pair = (lst1[i], lst2[j])  # tuple for each theoretically possible pair
                cart_res.append(cart_pair)
    return cart_res

def pairs(n,num_list):
    """
    The function contains nested loops,
    fix the element in the list and sum it with all the numbers that come after this element
    in such way we'll pass all the possible sums.
    :param n:the sum that we gonna find the numbers for
    :param num_list:the list from which we gonna find the pairs summing
    :return:list of all pairs that sum of their elements (from num_list) is equal to n
    """
    nice_pairs = []  # list for pairs that satisfy us
    for i in range(len(num_list)):
        for j in range(i, len(num_list)):
            if i != j:
                sum = num_list[i] + num_list[j]  # variable for sum of the current elements
                if sum == n:
                    nice_pairs.append([num_list[i], num_list[j]])  # appending the nice pair to the list
    return nice_pairs