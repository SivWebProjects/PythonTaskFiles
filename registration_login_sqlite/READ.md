I connected to sqlite3 and created a table in the login db database with columns for name, email, phone number, and password.
The home page is displayed first. It contains links to the login and registration pages. The urls "/register" and "/login" display the register and login pages, respectively.
When a user submits the registration form, the information is saved in the database and a success message is displayed; otherwise, an error message is displayed.
When a user submits the login form, check() function checks to see if the login credentials are present in the table. 
If they exist, their information will be displayed; otherwise, a registration form will be displayed.
