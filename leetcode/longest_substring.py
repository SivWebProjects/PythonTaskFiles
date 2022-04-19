
"""
Given a string s, find the length of the longest substring without repeating characters.
"""

string = input("Enter the string: ")
# Creating an empty set
charset = set()
left = 0
right = 0
res = 0

for right in range(len(string)):
    while string[right] in charset:
        charset.remove(string[left])
        left += 1
    charset.add(string[right])
    res = max(res, right - left + 1)
print("Length of longest substring without repeating characters is: ", res)
