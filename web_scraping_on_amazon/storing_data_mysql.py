import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

csv_file_path = '/home/neosoft/Documents/csv_files/amazon_books_2.csv'
books_data = pd.read_csv(csv_file_path, index_col=False)
print(books_data.head())

try:
    # Create a connection object to connect to MySQL, connect() constructor
    # creates a connection to the MySQL and returns a MySQLConnection object.
    conn = mysql.connect(host='localhost', database='web_scraping', user='root')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute("DROP TABLE IF EXISTS amazon_books;")
        print('Creating table....')
        # in the below line please pass the creating table statement which you want #to create
        cursor.execute(
                      """CREATE TABLE amazon_books(`Book Name` VARCHAR(600), Author VARCHAR(300), `Image Link` VARCHAR(600), 
                         Rating VARCHAR(200), `Customer Rating` VARCHAR(200), Price VARCHAR(200))""")
        print("Table is created....")
        # loop through the data frame
        for i, row in books_data.iterrows():
            sql = """INSERT INTO amazon_books(`Book Name`, Author, `Image Link`, Rating, `Customer Rating`, Price)
            VALUES (%s, %s, %s, %s, %s, %s);"""
            cursor.execute(sql, tuple(row))
            print("Record inserted", i)
            # The connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
except Error as e:
    print("Error while connecting to MySQL", e)
