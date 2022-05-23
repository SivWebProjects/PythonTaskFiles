# Import required packages
from pdf2image import convert_from_path
import cv2
import matplotlib.pyplot as plt
import pytesseract
import os
import re
import pandas as pd
import glob

# Convert pdf pages to image and store in images variable
# pdf_file_path = '/home/neosoft/Documents/recipe_data/pizzeria_recipes.pdf'
# images = convert_from_path(pdf_file_path)

# Saving pages of PDF as images
# for i, image in enumerate(images):
      # fname = "/home/neosoft/Documents/recipe_data/italian_recipes_images/image" + str(i) + ".png"
      # image.save(fname, "PNG")


# Using contours, crop the text block and extract text using pytesseract
def extract_text(folder_path):
    """
    Looping through identified contours of each image, text boxes are cropped
    and passed to ocr to read text, which is then stored in a list.

    Parameters:
        folder_path: The location of the images file from which the text will be extracted
    Result:
        recipes (list): The list contains all the pdf's recipe data.
    """
    recipes_list = []
    # listdir() method in python is used to get the list of all files and directories in the specified directory.
    # Loop over each image
    for image_path in os.listdir(folder_path):
        image_path = folder_path + "/" + "image1.png"

        # Read image from which text needs to be extracted
        img = cv2.imread(image_path)

        # Preprocessing the image starts

        # Convert the image to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Performing OTSU threshold
        ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (22, 22))

        # Applying dilation on the threshold image
        dilation = cv2.dilate(thresh1, rect_kernel, iterations=1)

        # Finding contours
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                               cv2.CHAIN_APPROX_NONE)

        # Creating a copy of image
        img2 = img.copy()
        each_recipe_text = []

        # Looping through the identified contours
        # Then rectangular part is cropped and passed on
        # to pytesseract for extracting text from it
        # and appended to the list
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)

            # Drawing a rectangle on copied image
            rect = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Crop the text block for giving input to OCR
            cropped = img2[y:y + h, x:x + w]
            plt.imshow(img2)

            # Apply OCR on the cropped image
            text = pytesseract.image_to_string(cropped)
            each_recipe_text.append(text)
        recipes_list.append(each_recipe_text)
    return recipes_list


# path to the images folder
folder_path = "/home/neosoft/Documents/recipe_data/recipes_images"
recipes_list = extract_text(folder_path)

# Remove trailing and leading spaces and store data in the list
titles_list, ingredients_list, procedure_list = [], [], []
for i in range(len(recipes_list)):
    procedure = ""
    each_recipe_length = len(recipes_list[i])
    if each_recipe_length == 5:
        title = recipes_list[i][1].strip()
        ingredients = recipes_list[i][3].strip()
        ingredients = re.sub("\n", " ", ingredients)
        procedure = recipes_list[i][2].strip()
        paragraph = re.sub("\n", " ", paragraph)
    else:
        title = recipes_list[i][1].strip()
        ingredients = recipes_list[i][-2].strip()
        ingredients = re.sub("\n", " ", ingredients)
        paragraphs = recipes_list[i][-3:2:-1]
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            paragraph = re.sub("\n", " ", paragraph)
            procedure += paragraph + " "
    titles_list.append(title)
    ingredients_list.append(ingredients)
    procedure_list.append(procedure)

# Create csv file to store recepies data
csv_file_path = "/home/neosoft/Documents/recipe_data/recipes_pdf2.csv"

# Create dataframe with 3 columns
columns_names = ['Recipe', 'Ingredients', 'Procedure']
recipe_dataframe = pd.DataFrame(columns=columns_names)

# Store recipe data to dataframe
recipe_dataframe['Recipe'] = titles_list
recipe_dataframe['Ingredients'] = ingredients_list
recipe_dataframe['Procedure'] = procedure_list
print(recipe_dataframe)

# Save data to csv file
# recipe_dataframe.to_csv(csv_file_path)
