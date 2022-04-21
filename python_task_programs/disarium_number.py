# Create a function that determines whether a number is a Disarium or not.

def finding_disarium(num):
    """
    Takes number as an input then sum of its digits powered with their respective position
    and print a disarium number when the given number is equal to the original number 
    else it prints not a disarium number.

    Parameters:
        num (int): An integer

    Returns:
        result (str): A string whether it is a disarium or not
    """
    list_of_digits = list(num)
    length = len(list_of_digits)
    sum = 0
    
    for i in range(length):
        sum += int(list_of_digits[i]) ** (i+1)

    if sum == int(num):
        result = "Given number " + num + " is a Disarium Number."
    else:
        result = "Given number " + num + " is not a Disarium Number."

    return result


number = input("Enter a number: ")

# Calling the function by passing number as an argument
result = finding_disarium(number)
print(result)
