daniellevin
336462874
Daniel_Levin

I discussed the exercise with: Peleg LabSupport

============================================================================
=  README for ex3: Loops, getting input from the user, lists, nestes loops =
============================================================================
This exercise is about using different types of loops and lists
It includes one file:
    ex3.py - different functions with use of loops and lists


==================
=  Description:  =
==================
Running the program 'ex3.py' will provide the access to the next functions:
    -create_list() - creating list
    -concat_list(str_list) - concatenating strings
    -average(num_list) - counting the average value of numbers from the list
    -cyclic(lst1, lst2) - defining if one list is cyclic permutation of another or not
    -histogram(n, num_list) - counting the histogram for numbers until n in list
    -prime_factors(n) - creating the list of prime factors of number n
    -cartesian(lst1, lst2) - creating the list of cartesian product of two lists of elements
    -pairs(n, num_list) - creating a list of pairs that sum of their elements gives n


======================
=  Special Comments  =
======================

What's up Doc?

Part D
Theoretical questions:

1. cyclic('abcd', 'bcda') - calling the function will return True. Algorithm that we`ve done didn`t change the list
    because it was one of condition of the question. So we didn`t really use that list is mutable. That`s why
    function can easily get strings (that are immutable by the way) as a parameters and all the other methods
    that we`ve used for lists are good for strings too. Strings 'abcd' and 'bcda' are indeed permutations of each other.
    This is the reason why function returns True.

2. histogram(3, [1, 2, 3, 4]) - the function will work and it will return list: [0, 1, 1].
    all the parameters are good so we just get the relevant histogram

3. prime_factors(0) - my function will return the list [0]. Hence n=0 the loop wont run
    "for i in range(MIN_PRIME_NUM, root_n + 1):" = "for i in range(2, 1):" - not defined
    because the step is still 1.
    So factor will always be 1, that`s why in the end of function the value of n will be appended to the list,
    and after that while will be stopped. So function returns [0].

4. pairs(2, [0, 0, 1, 1, 2, 2]) - the function will return the list [[0, 2], [0, 2], [0, 2], [0, 2], [1, 1]]
    Hence we didn`t treat cases when there are the same numbers in the given list, function will continue to find pairs,
     and the function will think that pair [1, 1] satisfies the condition. It`s really so by the way.
    Furthermore the algorithm is such that pair [0, 2] will be counted 4 times - twice for each 0.