NUM_OF_SPOONS_IN_CUP = 3.5 #the number of spoons in one cup

def convert_spoon_to_cup(num_of_spoons):
    """This is the function that returns the number of cups that contains the same volume
    of liquid like it's contained in the number of spoons that the fuction gets as a parameter"""
    num_of_cups = (num_of_spoons / NUM_OF_SPOONS_IN_CUP)
    return num_of_cups

#print(convert_spoon_to_cup(7))
