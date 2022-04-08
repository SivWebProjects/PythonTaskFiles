"""
Create a function that returns the majority vote in a list. A majority vote is 
an element that occurs > N/2 times in a list (where N is the length of the list).

Example:- majority_vote(["A", "A", "B"]) ➞ "A" 
majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A" 
majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
""" 

def finding_majority(lst):
    #return the majority elements in a list
    #that occurs greater than half of the length of the list times
    unique_ele = list(set(lst))
    majority_list = [item for item in unique_ele if lst.count(item) > (len(lst) // 2)]
    return majority_list


lst = input().split()
#print(lst)

#Calling the function and passing given list as an argument
majority_list = finding_majority(lst)

if len(majority_list) == 0:
    print("Majority Vote in the given list is None.")
else:
    print("Majority Vote in the given list is " + " ".join(majority_list) + ".")
