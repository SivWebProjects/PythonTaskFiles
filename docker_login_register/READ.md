For deploying a flask app on docker, I used the sqlite login and registration task. 
I connected to the login db database and opened the user details table in sqlite3, which had columns for name, email, phone number, and password. 
The urls "/" and /register/" take you to the login and registration pages, respectively.
If the entered email address does not already exist in the database, when a user submits the registration form, the information is saved in the database. 
If an email address does not exist, the registration page displays an error message; otherwise, their information is displayed.
The login validation() function checks to see if the login credentials are present in the table when a user submits the login form. 
If they exist, their information is shown; otherwise, an error message is displayed.
Following the creation of the flask app, the Dockerfile is created, which is a text document containing the commands used to assemble the image.
Later, I created an image, then a container for it, and then I pushed it to Docker Hub.
