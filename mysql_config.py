from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure database
db = yaml.safe_load(open("/home/neosoft/Documents/PythonFiles/flask/db.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
# app.config["MYSQL_PASSWORD"] = db["mysql_password"]
app.config["MYSQL_DB"] = db["mysql_db"]

# Create Mysql object
mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Fetch form data and storing in the variable
        user_details = request.form
        name = user_details["name"]
        email = user_details["email"]

        # post request to make an entry into database
        cur = mysql.connection.cursor() #
        cur.execute("INSERT INTO users(name, email_id) Values (%s, %s)", (name, email))

        # It save changes into database
        mysql.connection.commit()

        # Closing cursor
        cur.close()
        return "Success"

    else:
        return render_template("form.html")


@app.route("/user_details")
def displaying_result():
    cur = mysql.connect.cursor()
    result_value = cur.execute("SELECT * FROM users")
    if result_value > 0:
        user_details = cur.fetchall()

        return render_template("users_result.html", user_details=user_details)

    else:
        return "No records in the Users Table"


if __name__ == "__main__":
    app.run(debug=True)
