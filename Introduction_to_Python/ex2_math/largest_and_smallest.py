
def largest_and_smallest(num1, num2, num3):
    """This is the function that gets 3 numbers and returns 2 numbers:
    the maximum of them and the minimum of them"""
    if (num1 >= num2) and (num2 >= num3):
        return num1, num3
    elif (num1 <= num2) and (num2 <= num3):
        return num3, num1
    elif (num1 >= num3) and (num3 >= num2):
        return num1, num2
    elif (num1 <= num3) and (num3 <= num2):
        return num2, num1
    elif (num3 >= num1) and (num1 >= num2):
        return num3, num2
    return num2, num3

#largest_and_smallest(1, 3, 2)
#print(largest_and_smallest(1, 5, 10))