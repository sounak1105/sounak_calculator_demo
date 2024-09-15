

def add(a, b):   # function to perform addition
    result = a + b 
    return result

def multiply(a, b):     # function to perform multiplication
    result = a * b 
    return result

def substraction(a, b):     # function to perform substraction
    result = a - b 
    return result

def divide(a, b):       # function to perform division
    try:
        result=a/b

    except Exception as e:
        print(f'Error: {e}')
        
    return result

def remainder(a, b):        # function to find remainder when a number is divided by a certain number
    result = a % b 
    return result

def tothepower(a, b):       # function to find power
    result= a**b
    return result

def process_input():        # function to input values

    input1 = input("Enter A:")
    if("" == input1):
        print("invalid input. please enter a value of A")
        input1 = None
        return
    
    input2 = input("Enter B:")
    if("" == input2):
        print("invalid input. please enter a value of B")
        input2 = None
        return

    op = input("Enter Operation:")
    if ("" == op):
        print("invalid input. please enter a operation")
        op = None
        return

    return (input1, input2, op)

def calc( input1, input2, op):      # function to perform the real calculation
    if ((None == input1) or (None == input2) or (None == op)):
        print('please enter a valid number. input cannot be blank')
        return

    try:
        if ('+' == op):
            result = add(float(input1), float(input2))

        elif('*' == op):
            result = multiply(float(input1), float(input2))

        elif('-' == op):
            result = substraction(float(input1), float(input2))

        elif('/' == op):
            result = divide(float(input1), float(input2))

        elif('%' == op):
            result = remainder(float(input1), float(input2))

        elif('^' == op):
            result = tothepower(float(input1), float(input2))
        
        else:
            print("this operation does not exists")
            return

    except Exception as e:
        print(e)
    return result
    

def main():     # the main program takes place
    try:   
        while True:
            (input1, input2, op) = process_input()
            result=calc(input1, input2, op)
            print(f'{input1} {op} {input2} = {result}')
            a = input('do you wish to continue. press "y" for yes or "n" for no: ')
            if(a=='n' or a=='N'):
                break

    except Exception as e:
        print ( e )

# Starting point 
# if __name__ == "__main__":
main()