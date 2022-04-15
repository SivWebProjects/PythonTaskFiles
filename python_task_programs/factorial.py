# Create a function that takes an integer n and returns the factorial
# of factorials ... do it using recursive function

def finding_factorial(num):
    """
    Takes an integer number and find the factorial of that number 
    by calling itself again and again until the number is equals to zero.

        Parameters:
            num (int): An integer

        Returns:
            fact (int): Factorial of a number
    """
    if num == 0:  # Base case
        return 1

    else:
        return num * finding_factorial(num - 1)


def fact_of_fact(num):
    """
    Takes a whole number and determines the factorial of factorials of the given number
    by calling finding_factorial() function until the number equals to zero.

        Parameters:
            num (int): A whole number

        Returns:
            fact (int): Factorial of factorials of a number
    """
    fact = 1
    while num != 0:
        fact = finding_factorial(num) * fact
        num -= 1
           
    return fact


input_valid = True
num = 0

# Loop continues until gets a whole number as an input
while input_valid:
    try:
        num = int(input("Enter an whole number: "))
        if num < 0:
            print("Please enter an whole number 0 or greater")
            input_valid = True
        else:
            input_valid = False
    except ValueError:
        print("Please enter an whole number")
        input_valid = True

# Calling the function and passing given number as an argument
result = fact_of_fact(num)
print("Factorial of " + str(num) + " is " + str(result))
