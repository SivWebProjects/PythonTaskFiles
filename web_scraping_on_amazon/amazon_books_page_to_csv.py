# Importing required libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd

# Accessing the HTML content from webpage
url = "https://www.amazon.in/gp/bestsellers/books/"
response = requests.get(url)
if response.status_code == 200:
    print("Successfully connected to the website.")
else:
    print("Not connected to the website.")

# Parsing the HTML content
soup = BeautifulSoup(response.content, 'html5lib')

# Step 4: Searching and navigating through the parse tree
book_names, authors, images, ratings, customers_ratings, prices = [], [], [], [], [], []
table = soup.find('div', attrs={'class': 'p13n-gridRow _cDEzb_grid-row_3Cywl'})
if table is not None:
    for row in table.findAll('div', attrs={'class': 'zg-grid-general-faceout'}):
        book_name = row.img['alt']
        if book_name is not None:
            text = book_name
        else:
            text = "Unknown Product"
        book_names.append(text)
        author = row.find('a', attrs={'class': 'a-size-small a-link-child'})
        if author is not None:
            text = author.text
        else:
            author = row.find('span', attrs={'class': 'a-size-small a-color-base'})
            text = author.text
        authors.append(text)
        image = row.img['src']
        if image is not None:
            url = image
        else:
            url = "No Link"
        images.append(url)
        rating = row.find('span', attrs={'class': 'a-icon-alt'})
        if rating is not None:
            text = rating.text
        else:
            text = "-1"
        ratings.append(text)
        customer = row.find('div', attrs={'class': 'a-icon-row'})
        if customer is not None:
            customers_rated = customer.find('span', attrs={'class': 'a-size-small'})
            if customers_rated is not None:
                text = customers_rated.text
            else:
                text = "0"
                customers_ratings.append(text)
        else:
            text = "0"
        customers_ratings.append(text)
        price = row.find('span', attrs={'class': 'p13n-sc-price'})
        if price is not None:
            text = price.text
        else:
            text = "0.00"
        prices.append(text)

# Step 5: Creating Dataframe
column_names = ['Book Name', "Author", "Image Link", "Rating", "Customer Rating", "Price"]
books = pd.DataFrame(columns=column_names)
books['Book Name'] = book_names
books['Author'] = authors
books['Image Link'] = images
books['Rating'] = ratings
books['Customer Rating'] = customers_ratings
books['Price'] = prices
print(books)

# Step 6: Creating CSV file
csv_file_path = "/home/neosoft/Documents/csv_files/amazon_books.csv"
# new_file = open(csv_file_path, "x")
# Step 7: Storing data in a created csv file
# books.to_csv(csv_file_path)
