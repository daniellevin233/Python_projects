def two_largest(num1, num2, num3):
    """This is the function that gets 3 numbers
    and returns the 2 largest of them"""
    if (num1 >= num2) and (num2 >= num3):
        return num1, num2
    elif (num1 <= num2) and (num2 <= num3):
        return num3, num2
    elif (num1 >= num3) and (num3 >= num2):
        return num1, num3
    elif (num1 <= num3) and (num3 <= num2):
        return num2, num3
    elif (num3 >= num1) and (num1 >= num2):
        return num3, num1
    return num2, num1

def is_it_summer_yet(threshold, tem_day1, tem_day2, tem_day3):
    """This is the function that gets threshold and temperatures of 3 days
    and returns True if there are at least 2 days with temperature higher than threshold
    and returns False in opposite case - at best 1 day warmer than threshold"""
    warm_day1, warm_day2 = two_largest(tem_day1, tem_day2, tem_day3)#definition of 2 the warmest days to compare them with the threshold
    if (warm_day1 > threshold) and (warm_day2 > threshold):#we need at least 2 days out of 3 such that their temperature will be higher than thresholdy
        return True
    return False

print(is_it_summer_yet(7,5,-2,11))