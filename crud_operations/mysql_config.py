from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)


'''configure database'''
db = yaml.load(open("db.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_DB"] = db["mysql_db"]

mysql = MySQL(app)   # instance of mysql obj


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # fetch form data
        user_details = request.form
        name = user_details["nm"]
        email = user_details["mail"]

        cur = mysql.connection.cursor()   # post request to make an entry into db
        cur.execute("INSERT INTO userdetails(name, email) Values (%s, %s)", (name, email))
        mysql.connection.commit()     # it saves the changes in db
        cur.close()        # close cursor
        return "Success"
    else:
        return render_template("form.html")


@app.route("/user_details")
def result():
    cur = mysql.connect.cursor()
    value_store = cur.execute("SELECT * FROM userdetails")
    if value_store > 0:
        user_details = cur.fetchall()

        return render_template("user.html", user_details=user_details)

    else:
        return "No records found"


@app.route("/update_details", methods=["GET", "POST"])
def updating_data():
    # "PUT", "DELETE"]
    if request.method == "POST":
        # Fetch data from form and storing in the variable
        user_details = request.form
        old_name = user_details["name"]
        new_name = user_details["new_name"]
        old_email = user_details["email"]
        new_email = user_details["new_email"]

        cur = mysql.connection.cursor()

        if (old_name != "" and new_name != "") and (old_email == "" or new_email == ""):
            cur.execute("UPDATE userdetails SET name = (%s) WHERE name = (%s)", (new_name, old_name))

        elif (old_email != "" and new_email != "") and (old_name == "" or new_name == ""):
            cur.execute("UPDATE userdetails SET email = (%s) WHERE email = (%s))", (new_email, old_email))

        elif (old_name != "" and new_name != "") and (old_email != "" and new_email != ""):
            cur.execute("""UPDATE userdetails SET name = (%s), email = (%s)
                           WHERE name = (%s) AND email = (%s)""", (new_name, new_email, old_name, old_email))

        mysql.connection.commit()

        cur.close()
        print("Successfully Updated")

        return redirect('/user_details')

    else:
        return render_template("form2.html")


@app.route("/delete_details", methods=["GET", "POST"])
def deleting_data():
    # "PUT", "DELETE"]
    if request.method == "POST":
        # Fetch data from form and storing in the variable
        user_details = request.form
        name = user_details["name"]
        email = user_details["email"]

        cur = mysql.connection.cursor()

        if name != "" and email == "":
            cur.execute("DELETE FROM userdetails WHERE name = (%s)", [name])

        elif email != "" and name == "":
            cur.execute("DELETE FROM userdetails WHERE email = (%s)", [email])

        mysql.connection.commit()

        cur.close()
        print("Successfully Deleted")

        return redirect('/user_details')

    else:
        return render_template("form3.html")


if __name__ == "__main__":
    app.run(debug=True)