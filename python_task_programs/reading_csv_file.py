# Read a csv file, remove last 2 rows from it and create new csv file 
# using csv library not pandas

# csv means comma-separated values
import csv

# Open the text file in read mode
file = open("/home/neosoft/Documents/PythonFiles/venv/Name_Data_Dup.csv", "r")

# Creating a new csv file
new_file = open("Name_Data_Copied.csv", 'x')

data = csv.reader(file)
writer = csv.writer(new_file)

data_list = []

# Appending each row into a list
for row in data:
    data_list.append(row)

print("Original Data in CSV File: " + str(data_list))

length = len(data_list)
print("Length of list is: " + str(length))

# Writes all the rows except last two rows into the new file
for i in range(length - 2):
    writer.writerow(data_list[i])

# Closing the opened files
file.close()
new_file.close()
