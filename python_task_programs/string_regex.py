# "This#string%contains^special*characters&.";   
# Print string without all special characters from above string.

import re

string = input("Enter the string: ")

# Replacing special characters with space in the given string
string_without_special_chars = re.sub("[^a-zA-Z0-9]", " ", string)

# Count the number of special characters in the given string
count_of_special_chars = string_without_special_chars.count(" ")

print("String without all special characters in the given string is: " + string_without_special_chars)
print("Count of special characters in the given string is: " + str(count_of_special_chars))
