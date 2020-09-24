
def calculate_mathematical_expression(num1, num2, operation):
    """This is the function that gets two numbers and operation,
    and returns the result of this operation on this numbers"""
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            return None
        return num1 / num2
    return None#if the user inputs something that we don't know of, function returns None

def calculate_from_string(str_expression):
    """This is the function that gets string that contains mathematical expression
    and returns the result of this operation"""
    num1_str, operation_str, num2_str = str_expression.split()#determinating the variables in addition to the order that is appearing in the string
    return calculate_mathematical_expression(float(num1_str), float(num2_str), operation_str)


#print(calculate_mathematical_expression(10, 0, '/'))
#print(calculate_from_string('10 / 4'))