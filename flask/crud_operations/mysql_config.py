from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure database
db = yaml.safe_load(open("config.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_DB"] = db["mysql_db"]

# Create Mysql object
mysql = MySQL(app)


@app.route("/", methods=["GET", "POST"])
def index():
    """It takes name and email of the person and adds it to the mysql users database."""
    if request.method == "POST":
        # Fetch data from form and storing in the variables
        user_details = request.form
        name = user_details["name"]
        email = user_details["email"]

        # post request to make an entry into database
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name, email_id) Values (%s, %s)", (name, email))

        # It save changes into database
        mysql.connection.commit()

        # Closing cursor
        cur.close()
        print("Successfully Created")

        return redirect('/user_details')
    else:
        return render_template("form.html")


@app.route("/user_details")
def displaying_result():
    """It displays name and email of persons in mysql users database."""
    cur = mysql.connect.cursor()
    result_value = cur.execute("SELECT * FROM users")

    if result_value > 0:
        user_details = cur.fetchall()
        return render_template("users_result.html", user_details=user_details)
    else:
        return "No records in the Users Table"


@app.route("/update_details", methods=["GET", "POST"])
def updating_data():
    """It takes name and email of the person and new name or/and new email to update it to the mysql users database."""
    if request.method == "POST":
        # Fetch data from form and storing in the variables
        user_details = request.form
        old_name = user_details["name"]
        new_name = user_details["new_name"]
        old_email = user_details["email"]
        new_email = user_details["new_email"]

        cur = mysql.connection.cursor()

        if (old_name != "" and new_name != "") and (old_email == "" or new_email == ""):
            cur.execute("UPDATE users SET name = (%s) WHERE name = (%s)", (new_name, old_name))
        elif (old_email != "" and new_email != "") and (old_name == "" or new_name == ""):
            cur.execute("UPDATE users SET email_id = (%s) WHERE email_id = (%s))", (new_email, old_email))
        elif (old_name != "" and new_name != "") and (old_email != "" and new_email != ""):
            cur.execute("""UPDATE users SET name = (%s), email_id = (%s)
                           WHERE name = (%s) AND email_id = (%s)""", (new_name, new_email, old_name, old_email))

        mysql.connection.commit()

        cur.close()
        print("Successfully Updated")

        return redirect('/user_details')
    else:
        return render_template("form2.html")


@app.route("/delete_details", methods=["GET", "POST"])
def deleting_data():
    """It takes name or email of the person and delete the person
    details if the details exists in the mysql users database.
    """
    if request.method == "POST":
        # Fetch data from form and storing in the variables
        user_details = request.form
        name = user_details["name"]
        email = user_details["email"]

        cur = mysql.connection.cursor()

        if name != "" and email == "":
            cur.execute("DELETE FROM users WHERE name = (%s)", [name])
        elif email != "" and name == "":
            cur.execute("DELETE FROM users WHERE email_id = (%s)", [email])

        mysql.connection.commit()

        cur.close()
        print("Successfully Deleted")

        return redirect('/user_details')
    else:
        return render_template("form3.html")


app.run(debug=True)
