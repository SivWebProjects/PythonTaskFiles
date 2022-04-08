#"This#string%contains^special*characters&.";   
#I want string without all special characters from above string

import re

string = input("Enter the string: ")
string_without_special_chars = re.sub("[^a-zA-Z0-9]", " " , string)

# count the number of special characters in the given string
count_of_special_chars = string_without_special_chars.count(" ")

print("String without all special characters and number of special characters in the given string are: " + string_without_special_chars + " and " + str(count_of_special_chars))