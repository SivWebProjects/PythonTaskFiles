# create four list containing string and combine every element from each list in a single tuple
# example for two list  l1 =[1,2,3,4] l2 = [5,6,7,8]
# ans  =[(1,5),(2,6),(3,7),(4,8)] without using for loop

list1 =['six', 'two', 'three'] 
list2 = ['ball', 'pen', 'pencil']
list3 = ['ha', 'gh', 'rt', 'bn']
list4 = ['bhn', 'hfg', 'fhy', 'ase']

# combining every element from each list
print(list(zip(list1, list2, list3, list4)))