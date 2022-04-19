"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

# Taking list of integer numbers
nums = map(int, input("Enter space separated integers: ").split())

# Taking the target number
target = int(input("Enter the target number: "))

# Creating an empty dictionary
prev_map = {}  # value:index

for index, value in enumerate(nums):
    # Loop over list and added to the dictionary
    # if it is not present and print the indices of numbers
    # whose sum is equal to the given target number
    difference = target - value

    if difference in prev_map:
        print([prev_map[difference], index])
        break

    prev_map[value] = index
