# Read a text file ..try to find vowels and count it 
# Next in a dictionary put word as a key and number of times that word has occurred 
# in that text file as a value of that key

import re

# Open the text file in read mode
file = open("/home/neosoft/Documents/PythonFiles/venv/sample.txt", "r")
text = file.read()
text = text.lower()

vowel_count = 0
vowels_list = ['a', 'e', 'i', 'o', 'u']

for char in text:
    # Check if the character is already in list
    if char in vowels_list:
        vowel_count += 1
print("Total number of vowels in a text file are: "+str(vowel_count))


words=[]
words_dict={}

exp = re.sub("[.,']", "" , text)

for i in exp.split():
    if i == "":
        pass
    else:
        words.append(i)

    words_dict[i]=words.count(i)

print(words_dict)