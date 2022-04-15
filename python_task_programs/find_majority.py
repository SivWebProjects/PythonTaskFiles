"""
Create a function that returns the majority vote in a list. A majority vote is 
an element that occurs > N/2 times in a list (where N is the length of the list).

Example:- majority_vote(["A", "A", "B"]) ➞ "A" 
majority_vote(["A", "A", "A", "B", "C", "A"]) ➞ "A" 
majority_vote(["A", "B", "B", "A", "C", "C"]) ➞ None
""" 


def finding_majority(lst):
    """
    Returns the majority elements in a list
    that occurs greater than half of the length of the list times.
    
    Parameters:
        lst (list): A list consists of space separated strings
        
    Returns:
        majority_list (str): A string
    """
    unique_ele = list(set(lst))
    majority_list = [item for item in unique_ele if lst.count(item) > (len(lst) // 2)]
    
    return majority_list


lst = input('Enter space separated strings: ').split()

# Calling the function and passing given list as an argument
result = finding_majority(lst)

if len(result) == 0:
    print("Majority Vote in the given list is None.")
    
else:
    print("Majority Vote in the given list is " + str(result[0]) + ".")
