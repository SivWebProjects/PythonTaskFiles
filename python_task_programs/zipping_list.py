# Create four list containing string and combine every element from each list in a single tuple.
# Example for two list  l1 =[1,2,3,4] l2 = [5,6,7,8]
# answer  =[(1,5),(2,6),(3,7),(4,8)] without using for loop

list1 = input("Enter space separated strings: ").split()
list2 = input("Enter space separated strings: ").split()
list3 = input("Enter space separated strings: ").split()
list4 = input("Enter space separated strings: ").split()

# Combining every element from each list upto equal length of all lists
print(list(zip(list1, list2, list3, list4)))
