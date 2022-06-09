I accessed the user info table in the MySQL database, which contained columns for name, email, phone number, and password. The urls "/" and /register/" 
display the login and registration pages, respectively. When a user submits the registration form, the information is saved in the database if the entered 
email address does not already exist in the database. If an email address does not exist, an error message is displayed on the registration page; otherwise,
all records in the database are displayed. When a user submits the login form, the login validation() function checks to see if the login credentials are 
present in the table. If they exist, all of the records in the table are displayed; otherwise, an error message is displayed in the login form. When the records are 
displayed on the page, an authenticated user can create another account with a different email address, update the user's existing details, and delete the existing 
account using ajax, so the above operations can be completed without loading the page.

![Screenshot from 2022-05-05 23-47-48](https://user-images.githubusercontent.com/99475439/172769008-81b0647c-7c8c-47c6-b49f-b92a6915b432.png)
![Screenshot from 2022-05-05 23-47-30](https://user-images.githubusercontent.com/99475439/172769019-a605889b-c005-4e41-bc7c-9984e698d3c6.png)
![Screenshot from 2022-05-05 23-48-28](https://user-images.githubusercontent.com/99475439/172769033-b0fbfda7-9d1a-40d2-81c3-e7c6f903ee96.png)
![Screenshot from 2022-05-05 23-48-06](https://user-images.githubusercontent.com/99475439/172769039-fb689103-b08d-4d8a-93e4-ac4a8343056c.png)
![Screenshot from 2022-05-10 11-04-16](https://user-images.githubusercontent.com/99475439/172769057-970d57ed-ccb4-477e-b393-25e66a943ab7.png)
