I accessed the user info table in the MySQL database, which contained columns for name, email, phone number, and password. The urls "/" and /register/" 
display the login and registration pages, respectively. When a user submits the registration form, the information is saved in the database if the entered 
email address does not already exist in the database. If an email address does not exist, an error message is displayed on the registration page; otherwise,
all records in the database are displayed. When a user submits the login form, the login validation() function checks to see if the login credentials are 
present in the table. If they exist, all of the records in the table are displayed; otherwise, an error message is displayed in the login form. When the records are 
displayed on the page, an authenticated user can create another account with a different email address, update the user's existing details, and delete the existing 
account using ajax, so the above operations can be completed without loading the page.
