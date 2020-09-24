import math

def quadratic_equation(a, b, c):
    """This is the function that gets as parameters three coefficients for the square equation
    and returns its roots"""
    discr = b**2 - 4*a*c #determinating variable for the discriminant formula
    if discr > 0:#if the discriminant bigger than 0, the equation has 2 roots
        return (-b + math.sqrt(discr))/ (2*a), (-b - math.sqrt(discr))/ (2*a)
    elif discr == 0:#if the discriminant equals 0, then the equation has 1 root
        if (b == 0) and (c == 0):#if b and c are 0 we don't need to use the  formula, the solution is always 0, I assume that a!=0
            return 0, None
        return (-b/2), None
    return None, None#otherwise, if the discriminant less then 0, the equation has no solutions

def quadratic_equation_user_input():
    """This is the function that gets as input the coefficients for the square equation from the user
    and returns its solution"""
    user_a, user_b, user_c = input('Insert coefficients a, b and c:').split() # definition of variables for the users' coefficients
    root1, root2 = quadratic_equation(float(user_a), float(user_b), float(user_c)) # definition of variables for the equation roots
    if root1 == None:
        return print('The equation has no solution')
    if root2 == None:
        return print('The equation has 1 solution:', root1)
    return print('The equation has 2 solutions:', root1, 'and', root2)


#quadratic_equation_user_input()
#print(quadratic_equation(1, 0, 0))