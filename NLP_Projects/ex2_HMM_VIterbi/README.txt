matancha, daniellevin
===============================================================================
Matan Toledano, ID 313591935, matan.toledano@mail.huji.ac.il
Daniel Levin, ID 336462874, daniil.levin@mail.huji.ac.il
===============================================================================

                           Exercise 2, HMM model and Viterbi algorithm
                           ------------------------------------------------


Submitted Files
---------------
ex2.py - Main flow of program running all the requested algorithms and printing the results to the console
Pseudowords.py - Class dealing with initialization with pseudowords
Unigram.py - learning Class representing HMM algorithm for unigram using MLE approach
Bigram.py - learning Class representing HMM algorithm for unigram using MLE approach
README - this file

Answers
-------
For tagging unknown words in Bigram model, we used the distribution of the tags over the training set
and relying on this distribution fetched tags. The current column is filled up with the same probabilities,
thus reflecting the randomness of chosen tag.
