import pandas as pd
import psycopg2

csv_file_path = '/home/neosoft/Documents/csv_files/amazon_books.csv'
books_data = pd.read_csv(csv_file_path, index_col=False)
print(books_data.head())

try:
    # Connect to your PostgresSQL database on a remote server
    conn = psycopg2.connect(host="127.0.0.1", port="5432", database="web_scraping", user="postgres",
                            password="xxx")
    print(conn)
    if conn is not None:
        # Open a cursor to perform database operations
        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS amazon_books")
        cursor.execute(
                      """CREATE TABLE amazon_books("Book Name" VARCHAR(600), Author VARCHAR(300), "Image Link" 
                      VARCHAR(600), Rating VARCHAR(200), "Customer Rating" VARCHAR(200), Price VARCHAR(200))""")
        print("Table is created....")
        # loop through the data frame
        for i, row in books_data.iterrows():
            sql = """INSERT INTO amazon_books("Book Name", Author, "Image Link", Rating, "Customer Rating", Price)
                     VALUES (%s, %s, %s, %s, %s, %s)"""
            cursor.execute(sql, tuple(row))
            # The connection is not auto committed by default, so we must commit to save our changes
            conn.commit()
        conn.close()
except (Exception, psycopg2.DatabaseError) as e:
    print("Error while connecting to PostgresSQL", e)
