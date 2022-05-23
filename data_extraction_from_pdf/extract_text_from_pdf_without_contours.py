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


# Extract text using pytesseract
def extract_text(folder_path):
    """
    Text is extracted by looping through each image,
    passing it to ocr, and storing it in a list.

    Parameters:
        folder_path: The location of the images file from which the text will be extracted
    Result:
        recipes (list): The list contains all the pdf's recipe data.
    """
    recipes = []
    # Loop over each image
    for image_path in os.listdir(folder_path):
        image_path = folder_path + "/" + image_path
        # Read image from which text needs to be extracted
        image = cv2.imread(image_path)

        # Apply Pytesseract OCR on the image
        text = pytesseract.image_to_string(image)
        recipes.append(text)
    return recipes


# path to the images folder
folder_path = "/home/neosoft/Documents/recipe_data/recipes_images_2"
recipes = extract_text(folder_path)


# Remove trailing and leading spaces and store data in the list
def getting_recipe_details(recipes):
    """
    By looping through each recipe, recipe data is
    divided into titles, ingredients, and procedures.

    Parameters:
        recipes (list): The list contains all the pdf's recipe data.
    Result:
        recipes_names (list): The list contains all the recipes' names.
        recipes_ingredients (list): The list includes all the recipes' ingredients.
        recipes_procedures (list): The list contains all the recipes' procedures.
    """
    recipes_names, recipes_ingredients, recipes_procedures = [], [], []
    numbers_list = list(map(str, range(10)))
    for i in range(len(recipes)):
        content_list = re.split("\n\n", recipes[i])
        ingredients = ""
        procedure = ""
        for j in range(len(content_list)):
            if len(content_list[j]) > 2:
                if j == 0:
                    title = content_list[0].strip()
                else:
                    text = content_list[j]
                    if text == title or text[-6:] == "\n\x0c":
                        break
                    else:
                        text = re.split("", content_list[j])
                        first_char = content_list[j][0: 1]
                        if "." not in text or first_char in numbers_list:
                            ingredient = content_list[j].strip()
                            ingredient = re.sub("\n", " ", ingredient)
                            ingredients += ingredient + " "
                        else:
                            paragraph = content_list[j].strip()
                            paragraph = re.sub("\n", " ", paragraph)
                            procedure += paragraph + " "
        recipes_names.append(title)
        recipes_ingredients.append(ingredients)
        recipes_procedures.append(procedure)
    return recipes_names, recipes_ingredients, recipes_procedures


recipes_names, recipes_ingredients, recipes_procedures = getting_recipe_details(recipes)

csv_file_path = "/home/neosoft/Documents/recipe_data/recipes_pdf2.csv"

# Create dataframe with 3 columns
columns_names = ['Recipe', 'Ingredients', 'Procedure']
recipe_dataframe = pd.DataFrame(columns=columns_names)
print(recipe_dataframe.shape)

# Store recipe data to dataframe
recipe_dataframe['Recipe'] = recipes_names
recipe_dataframe['Ingredients'] = recipes_ingredients
recipe_dataframe['Procedure'] = recipes_procedures
print(recipe_dataframe)

# Save data to csv file
# recipe_dataframe.to_csv(csv_file_path)
