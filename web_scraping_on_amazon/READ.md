Using the beautifulsoup library, I performed web scraping on the Amazon books page. "https://www.amazon.in/gp/bestsellers/books/" is 
the page's url. First, I test whether the page has permission to extract html data by sending a request to it through the requests library. 
We have access if the status code is 200; otherwise, we do not. After that, use the html5lib library to parse the HTML text. Then, using 
html elements, collect the book title, author, image link, ratings, customer ratings, and price, and save it in a list. Later, 
I created a csv file and saved the information in it.
