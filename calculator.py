

def add(a, b):
    result = a + b 
    return result

def multiply(a, b):
    result = a * b 
    return result

def substraction(a, b):
    result = a - b 
    return result

def divide(a, b):
    if (b!=0):
        result = a / b
    else:
        print("invalid: denominator cannot be 0") 
        return
    
    return result

def remainder(a, b):
    result = a % b 
    return result

def tothepower(a, b):
    result= a**b
    return result

def process_input():
    # calculator
    input1 = input("Enter A:")
    if("" == input1):
        print("invalid input. please enter a value of A")
        input1 = None
    
    input2 = input("Enter B:")
    if("" == input2):
        print("invalid input. please enter a value of B")
        input2 = None

    op = input("Enter Operation:")
    if ("" == op):
        print("invalid input. please enter a operation")
        op = None

    return (input1, input2, op)

def main():
    (input1, input2, op) = process_input()
    if ((None == input1) or (None == input2) or (None == op)):
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

        print(f'{input1} {op} {input2} = {result}')

    except Exception as e:
        print(e)

     
# Starting point 
# if __name__ == "__main__":
main()