#Create a function that determines whether a number is a Disarium or not.

def finding_disarium(num):
    #takes number as input then sum of its digits powered with their respective position 
    #and print a disarium number when the given number is equal to the original number 
    #else it print not a disarium number
    list_of_digits = list(num)
    length = len(list_of_digits)
    sum = 0

    for i in range(length):
        sum += int(list_of_digits[i]) ** (i+1)
    
    if sum  == int(num):
        print("Given number " + num + " is a Disarium Number.")  
    else:
        print("Given number " + num + " is not a Disarium Number.")


number = input("Enter a number: ")
finding_disarium(number)