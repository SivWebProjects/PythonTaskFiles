I ran crud operations on the mysql database.
1) When the get method is encountered by default, the form is displayed on the web page.
2) When the url is "/user_details," all of the records in the database table are displayed as a table.
3) When the form is submitted, a post request is sent, which connects to the MySQL database and stores the 
   information entered by the user in the form and navigates to "/user_details."
4) When the url is "/update_details" and the get request is received by default, the update form is displayed. 
   If the request is post, it replaces the users existing name and email with new values taken from the form and navigates to          "/user_details."
5) The deletion form is displayed when the url is "/delete_details." If the request is posted, the table's user details 
   are deleted based on the name or email entered by the user in the form, and the user is navigated to "/user_details."
