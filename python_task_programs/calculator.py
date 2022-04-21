# 1. create a python module, add function for addition, subtraction, multiplication and division separately in one file
# 2. second file will import any function from above
# 3. give user input to choose function as well as to giving values for math operations until user says stop

# Importing all functions from arithmetic_module
from arithmetic_module import *

char = 'y'
operations = ['+', '-', '*', '/']
char_list = ['y', 'Y', 'n', 'N']
result = 0

while char == 'y' or char == 'Y':
    is_num1_valid = True
    is_num2_valid = True

    operation = input('Please enter the operator + for addition, - for subtraction, '
                      '* for multiplication and / for division: ')

    # It iterates until user enters correct operator
    while operation not in operations: 
        print("Please enter a valid math operator")
        operation = input()

    # It iterates until user enters integer number
    while is_num1_valid:
        try:
            first_num = int(input('Enter first integer number: '))
            is_num1_valid = False
            break
        except ValueError:
            print("Please enter a valid integer number")
            is_num1_valid = True

    # It iterates until user enters integer number
    while is_num2_valid:
        try:
            second_num = int(input('Enter second integer number: '))
            is_num2_valid = False
            break
        except ValueError:
            print("Please enter a valid integer number")
            is_num2_valid = True

    if operation == '+':
        result = sum(first_num, second_num)
    elif operation == '-':
        result = subtraction(first_num, second_num)
    elif operation == '*':
        result = multiplication(first_num, second_num)
    elif operation == '/':
        try:
            result = division(first_num, second_num)
        except ZeroDivisionError:
            result = "Infinity"
            print("Denominator cannot be a zero")

    print("Result of " + str(first_num) + operation + str(second_num) + " = " + str(result))

    char = input("If you want to continue enter 'y' or 'Y' or else then enter 'n' or 'N': ")
    while char not in char_list:
        print("Please enter a valid letter either 'y' or 'n': ")
        char = input()

    if char == 'n' or char == 'N':
        break
    else:
        continue
