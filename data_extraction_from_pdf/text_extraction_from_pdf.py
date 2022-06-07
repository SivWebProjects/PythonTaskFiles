from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from pdf2image import convert_from_path
import cv2
import pytesseract
import os
import re
import pandas as pd

pdf_files = ["/home/neosoft/Documents/recipe_data/crockpot_recipes.pdf",
             "/home/neosoft/Documents/recipe_data/italian_recipes.pdf",
             "/home/neosoft/Documents/recipe_data/barbecue_recipes.pdf"]
recipes = []
recipes_names, recipes_ingredients, recipes_procedures = [], [], []


def pdf_type(fname):
    """
    It determines whether the pdf is electronic or not based on the font property.
    :param fname: The location of the pdf file
    :return: str: The pdf type is returned.
    """
    e_pages = []
    image_pages = []
    page_num = 0
    with open(fname, 'rb') as infile:
        for page in PDFPage.get_pages(infile):
            page_num += 1
            if 'Font' in page.resources.keys():
                e_pages.append(page_num)
            else:
                image_pages.append(page_num)
    if page_num == len(e_pages):
        return "Electronic PDF"
    elif page_num == len(image_pages):
        return "Image PDF"
    else:
        return "Not a valid document"


# Reading texts from electronic pdf using pdfminer library and storing data in list
def pdf_to_text(pdf_file_name):
    """
    Reading texts by looping through each page of the PDF and storing them in a list.

    Parameters:
        pdf_file_name: The location of the pdf file from which the text will be extracted
    Result:
        recipes (list): The list contains all the pdfs' recipe data.
    """
    # PDFMiner boilerplate
    rsrcmgr = PDFResourceManager()
    return_string = StringIO()
    device = TextConverter(rsrcmgr, return_string, codec='utf-8', laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Extract text
    pdf = open(pdf_file_name, 'rb')
    page_no = 5
    # Looping through each page
    for page_number, page in enumerate(PDFPage.get_pages(pdf)):
        if page_number == page_no:
            interpreter.process_page(page)
            # Get text from StringIO
            data = return_string.getvalue()
            recipes.append(data)
            return_string.truncate(0)
            return_string.seek(0)
            page_no += 1
    pdf.close()
    return recipes


def extract_text(folder_path):
    """
    Text is extracted by looping through each image,
    passing it to ocr, and storing it in a list.

    Parameters:
        folder_path: The location of the images file from which the text will be extracted
    Result:
        recipes (list): The list contains all the pdfs recipes' data.
    """
    # recipes = []
    # Loop over each image
    for image_path in os.listdir(folder_path):
        image_path = folder_path + "/" + image_path
        # Read image from which text needs to be extracted
        image = cv2.imread(image_path)

        # Apply Pytesseract OCR on the image
        text = pytesseract.image_to_string(image)
        recipes.append(text)
    return recipes


def getting_recipe_details(recipes, start_len, end_len):
    """
    By looping through each recipe, recipe data is
    divided into titles, ingredients, and procedures.

    Parameters:
        recipes (list): The list contains all the pdfs' recipe data.
        start_len (int): The starting length of the recipe list. 
        end_len (int): The recipe list's final length.
    Result:
        recipes_names (list): The list contains all the recipes' names.
        recipes_ingredients (list): The list includes all the recipes' ingredients.
        recipes_procedures (list): The list contains all the recipes' procedures.
    """
    numbers_list = list(map(str, range(10)))
    for i in range(start_len, end_len):
        content_list = re.split("\n\n", recipes[i])
        ingredients = ""
        procedure = ""
        for j in range(len(content_list)):
            if len(content_list[j]) > 2:
                if j == 0:
                    name = content_list[0].strip()
                else:
                    text = content_list[j]
                    if text == name or text[-6:] == "\n\x0c":
                        break
                    else:
                        text = re.split("", content_list[j])
                        first_char = content_list[j][0:1]
                        if "." not in text or first_char in numbers_list or ":" in text[-1]:
                            ingredient = content_list[j].strip()
                            ingredient = re.sub("\n", ", ", ingredient)
                            ingredients += ingredient + " "
                        else:
                            paragraph = content_list[j].strip()
                            paragraph = re.sub("\n", " ", paragraph)
                            procedure += paragraph + " "
        recipes_names.append(name)
        recipes_ingredients.append(ingredients)
        recipes_procedures.append(procedure)


for pdf_file_path in pdf_files:
    result = pdf_type(pdf_file_path)
    print(pdf_file_path + " " + result)
    if result == "Electronic PDF":
        # Passing the pdf file path to the function
        start_len = len(recipes)
        pdf_to_text(pdf_file_path)
        end_len = len(recipes)
        getting_recipe_details(recipes, start_len, end_len)
    elif result == "Image PDF":
        pdf_file_path = '/home/neosoft/Documents/recipe_data/italian_recipes.pdf'
        images = convert_from_path(pdf_file_path)
        # Passing the pdf file path to the function
        recipes = extract_text(pdf_file_path)
        start_len = len(recipes)
        pdf_to_text(pdf_file_path)
        end_len = len(recipes)
        getting_recipe_details(recipes, start_len, end_len)
    else:
        print(result + ". Please provide a valid pdf.")

if len(recipes_names) != 0:
    columns_names = ['Recipe', 'Ingredients', 'Procedure']
    recipe_dataframe = pd.DataFrame(columns=columns_names)
    recipe_dataframe['Recipe'] = recipes_names
    recipe_dataframe['Ingredients'] = recipes_ingredients
    recipe_dataframe['Procedure'] = recipes_procedures
    print(recipe_dataframe.shape)
