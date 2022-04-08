#Create a function that takes an integer n and returns the factorial 
#of factorials ..do it using recursive function

def finding_factorial(num):
    #takes a whole number
    #determines the factorial of factorials of the given number
    #by calling itself again and again until the number equals to 0
    #and returns the result
    
    if num == 0: #base case 
        return 1
    else:
        return num * finding_factorial(num - 1)

def fact_of_fact(num):
    fact = 1

    while num !=0:
        fact =  finding_factorial(num) * fact
        num -= 1
           
    return fact


input_valid = True

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

#Calling the function and passing given number as an argument
result = fact_of_fact(num)
print("Factorial of " + str(num) + " is " + str(result))