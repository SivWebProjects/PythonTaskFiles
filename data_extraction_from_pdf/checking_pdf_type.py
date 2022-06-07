from pdfminer.pdfpage import PDFPage

pdf_files = ["/home/neosoft/Documents/recipe_data/crockpot_recipes.pdf",
             "/home/neosoft/Documents/recipe_data/italian_recipes.pdf",
             "/home/neosoft/Documents/recipe_data/barbecue_recipes.pdf"]


def pdf_type(pdf_file_path):
    """
    It determines whether the pdf is electronic or not based on the font property.
    :param fname: The location of the pdf file
    :return: str: The pdf type is returned.
    """
    e_pages = []
    image_pages = []
    page_num = 0
    with open(pdf_file_path, 'rb') as infile:
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

      
for pdf_file_path in pdf_files:
    result = pdf_type(pdf_file_path)
    print(result)
    
