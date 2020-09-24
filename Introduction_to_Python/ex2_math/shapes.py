import math
CHOOSE_MESSAGE = 'Choose shape (1=circle, 2=rectangle, 3=trapezoid):'

def circle_area(circle_rad):
    """The function gets the radius as a parameter
    and returns the circle area"""
    return math.pi*circle_rad**2

def rect_area(rect_side1, rect_side2):
    """The function gets the sides of the rectangle as a parameter
    and returns the rectangle area"""
    return rect_side1*rect_side2

def trap_area(basis1, basis2, height):
    """The function gets the bases and the height of the trapezoid as a parameter
    and returns the trapezoid area"""
    return ((basis1 + basis2)/2)*height

def check_shape(shape):
    """The function gets the shape that user've input
    and check if this shape exist.Then if yes, it asks the user to input his parameters for the shapes
    and calls the function that counts the neccesary area. If no it returns error"""
    if shape == 1:
        user_circle_rad = float(input())#user inputs the radius of the circle
        return circle_area(user_circle_rad)
    elif shape == 2:
        user_rect_side1 = float(input())#user inputs the first side of rectangle
        user_rect_side2 = float(input())#user inputs the second side of rectangle
        return rect_area(user_rect_side1, user_rect_side2)
    elif shape == 3:
        user_basis1 = float(input())#user inputs the first basis of trapezoid
        user_basis2 = float(input())#user inputs the second basis of trapesoid
        user_height = float(input())#user inputs the height of the trapesoid
        return trap_area(user_basis1, user_basis2, user_height)
    return None #if the user input neither '1' neither '2' neither '3', None will be returned

def shape_area():
    """This is the main function that asks the user to choose the shape
    and returns the area of the shape that was chosen"""
    user_shape = input(CHOOSE_MESSAGE)#Here the user choose the shape that he would count the area for
    return check_shape(float(user_shape))

#shape_area()
#print(shape_area())