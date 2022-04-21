# Read a csv file, remove last 2 rows from it and create update_delete_ajax_jquery csv file
# using csv library not pandas

# csv means comma-separated values
import csv

# Open the text file in read mode
file = open("/home/neosoft/Documents/PythonFiles/venv/name_data.csv", "r")

# Creating a update_delete_ajax_jquery csv file
new_file = open("name_data_copy.csv", 'x')

data = csv.reader(file)
writer = csv.writer(new_file)

data_list = []

# Appending each row into a list
for row in data:
    data_list.append(row)

print("Original Data in CSV File: " + str(data_list))

length = len(data_list)
print("Length of list is: " + str(length))

# Writes all the rows except last two rows into the update_delete_ajax_jquery file
for i in range(length - 2):
    writer.writerow(data_list[i])

# Closing the opened files
file.close()
new_file.close()
