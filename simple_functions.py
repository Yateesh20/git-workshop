# Custom python functions

def double_number(a):
    """This function performs addition operation with the number provided by itself resulting in doubleing the number"""
    return a+a

def square_number(a):
    """THis function performs multiplication opertration with the number provided by itself resulting in squraing the number"""
    return a*a

def print_message(time, function, result):
    """This functions prints the message for the functions above about the value before and after the operation is performed
        time : string value ,before or after the operation
        function : string value, name of the function used
        result : numeric value, value obtained after the operation.      
    """
    print(f'Value {time} {function} : {result}')

