

import traceback
import re

# Switch to print the stack trace in case of exception
log_err_traces = False

"""
Using REGEX to check the type
"""
def is_integer(value: str) -> bool:
    """Check if the string represents an integer."""
    return re.fullmatch(r'-?\d+', value) is not None

def is_float(value: str) -> bool:
    """Check if the string represents a float."""
    return re.fullmatch(r'-?\d+\.\d+', value) is not None or re.fullmatch(r'-?\d+\.\d+e[-+]?\d+', value) is not None

def is_bool(value: str) -> bool:
    """Check if the string represents a boolean."""
    return value.lower() in ['true', 'false']

def is_complex(value: str) -> bool:
    """Check if the string represents a complex number."""
    pattern = r'^[+-]?(\d+(\.\d+)?|\.\d+)([+-](\d+(\.\d+)?|\.\d+)j)?$'
    return re.fullmatch(pattern, value) is not None

def is_str(value: str) -> bool:
    """Check if the value contains only alphabetic characters."""
    return re.fullmatch(r'^[A-Za-z]+$', value) is not None

"""
Custom exception class
"""
class customException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


def add(a, b):
    result = a + b 
    return result

def multiply(a, b):
    result = a * b 
    return result

def substract(a, b):
    result = a - b 
    return result

def divide(a, b):
    result = a / b
    return result

def remainder(a, b):
    result = a % b 
    return result

def power(a, b):
    result = a ** b
    return result

"""
Template function for different datatype handling
"""
def create_int_fn(name):
    def int_template(input1: int, input2: int, func) -> int:
        return func(input1, input2)
    globals()[name] = int_template

def create_float_fn(name):
    def float_template(input1: float, input2: float, func) -> float:
        return func(input1, input2)
    globals()[name] = float_template

def create_str_fn(name):
    def str_template(input1: str, input2: str, func) -> str:
        return func(input1, input2)
    globals()[name] = str_template

def create_bool_fn(name):
    def bool_template(input1: bool, input2: bool, func) -> bool:
        return func(input1, input2)
    globals()[name] = bool_template

def create_complex_fn(name):
    def complex_template(input1: complex, input2: complex, func) -> complex:
        return func(input1, input2)
    globals()[name] = complex_template

"""
Create functions for different datatype from template
"""
create_int_fn('add_int')
create_int_fn('multiply_int')
create_int_fn('substract_int')
create_int_fn('divide_int')
create_int_fn('remainder_int')
create_int_fn('power_int')

create_float_fn('add_float')
create_float_fn('multiply_float')
create_float_fn('substract_float')
create_float_fn('divide_float')
create_float_fn('remainder_float')
create_float_fn('power_float')

create_str_fn('add_str')
create_str_fn('multiply_str')
create_str_fn('substract_str')
create_str_fn('divide_str')
create_str_fn('remainder_str')
create_str_fn('power_str')

create_bool_fn('add_bool')
create_bool_fn('multiply_bool')
create_bool_fn('substract_bool')
create_bool_fn('divide_bool')
create_bool_fn('remainder_bool')
create_bool_fn('power_bool')

create_complex_fn('add_complex')
create_complex_fn('multiply_complex')
create_complex_fn('substract_complex')
create_complex_fn('divide_complex')
create_complex_fn('remainder_complex')
create_complex_fn('power_complex')

"""
Template function for different operation
"""
def create_op_fn(name):
    def op_template(input1, input2, func):
        result = None

        func_suffix = name.split('_')[0]
        if is_integer(input1) and is_integer(input2):
            result = globals()[func_suffix + '_int'](int(input1), int(input2), func)
        elif is_float(input1) and is_float(input2):
            result = globals()[func_suffix + '_float'](float(input1), float(input2), func)
        elif is_bool(input1) and is_bool(input2):
            result = globals()[func_suffix + '_bool'](bool(input1), bool(input2), func)
        elif is_complex(input1) and is_complex(input2):
            result = globals()[func_suffix + '_complex'](complex(input1), complex(input2), func)
        elif is_str(input1) or is_str(input2):
            result = globals()[func_suffix + '_str'](str(input1), str(input2), func)
        else:
            raise customException("Type not supported")
        return result
    globals()[name] = op_template

"""
Create function for different operation from template
"""
create_op_fn('add_op')
create_op_fn('multiply_op')
create_op_fn('substract_op')
create_op_fn('divide_op')
create_op_fn('remainder_op')
create_op_fn('power_op')

"""
calulates the result using two operand and an operator
Returns:
    input1 : First operand
    input2 : Second operand
    op     : Operator
Raises:
    customException: If operation is not supported
"""
def perform_op(input1, input2, op):
    result = None
    try:
        if ('+' == op):
            result = add_op(input1, input2, add)
        elif('*' == op):
            result = multiply_op(input1, input2, multiply)
        elif('-' == op):
            result = substract_op(input1, input2, substract)
        elif('/' == op):
            result = divide_op(input1, input2, divide)
        elif('%' == op):
            result = remainder_op(input1, input2, remainder)
        elif('^' == op):
            result = power_op(input1, input2, tothepower)
        else:
            raise customException("[ERROR] operation is not supported")
    except Exception as e:
        raise
    return result

"""
Takes two input values and an operation from user
Returns:
    input1 : First operand
    input2 : Second operand
    op     : Operator
Raises:
    customException: If empty inputs are provided
"""
def process_input():
    try:
        input1 = input("Enter A:")
        if("" == input1 or None == input1):
            raise customException("Invalid input. please enter a value of A")
    
        input2 = input("Enter B:")
        if("" == input2 or None == input2):
            raise customException("Invalid input. please enter a value of B")

        op = input("Enter Operation:")
        if ("" == op or None == input2):
            raise customException("Invalid input. please enter a operation")
    except Exception as e:
        raise

    return (input1, input2, op)

"""
Performs calculation using two operand and a operator

Input:
    input1 : First operand
    input2 : Second operand
    op : Operator

Returns:
    result : Operation result

"""
def calc( input1, input2, op):      # function to perform the real calculation
    result = perform_op(input1, input2, op)
    return result

def print_header():
    print('------------------------------------------------------------------')
    print('                          Calculator                              ')
    print('Supported datatypes  : int, float, bool, complex, str             ')
    print('Supported op         : +, -, *, /, %, ^ (power)                   ')
    print('Only support operation with same type and if permitted            ')
    print('------------------------------------------------------------------')

def main():
    print_header()
    valid_inputs = ['y', 'n', ""]
    while True:
        try:
            # Take inputs
            (input1, input2, op) = process_input()
            # Perform calculation
            result=calc(input1, input2, op)

            print(f'{input1} {op} {input2} = {result}')
        except Exception as e:
            if log_err_traces:
                traceback.print_exception(type(e), e, e.__traceback__)
            else:
                print(f'[ERROR] {e}')
        finally:
            # Ask user to continue
            query_str = (
                         "Do you wish to continue? "
                         "[y / n] (Default y): "
                        )
            a = input(query_str)
            # Loop till a valid input is given
            while (a.lower() not in valid_inputs):
                a = input(query_str)
            # Break if the user doesn't want to continue
            if(a.lower() =='n'):
                break

if __name__ == "__main__":
    main()