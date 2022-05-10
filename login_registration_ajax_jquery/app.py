from flask import Flask, render_template, request, jsonify
import mysql.connector
from flask_mysqldb import MySQL, MySQLdb

app = Flask(__name__)

# Creating a secret key
app.secret_key = "caircocoders-ednalan"

# Connecting to the database
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'flaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def login():
    """this function navigates to the login page"""
    return render_template("login_form.html")


@app.route('/register/')
def register():
    """this function navigates to the register page"""
    return render_template("registration_form.html")


@app.route('/login_validation', methods=['POST'])
def login_validation():
    """it gets login details from the user and compare with the database data.
    if details are matched it goes to further else it returns the error text"""
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    email = request.form.get('email')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM user_info WHERE email LIKE (%s) AND password LIKE (%s)""", (email, password))
    users = cursor.fetchall()
    print(users)
    if len(users) > 0:
        return index()
    else: 
        message = "Your don't have an account. Please create account using below link."
        return render_template("login_form.html", msg=message)
    

@app.route('/add_user', methods=["POST"])
def add_user():
    """it takes required details from the user and store details
    into the database table."""
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    name = request.form.get('name')
    email = request.form.get('email')
    ph_no = request.form.get('ph_no')
    password = request.form.get('password')
    cursor.execute("""SELECT * FROM user_info WHERE email LIKE %s""", [email])
    record = cursor.fetchall()
    print(record)
    if len(record) > 0:
        msg = "Email is already exists. Create account using another email."
        return render_template('registration_form.html', msg=msg)
    else:
        cursor.execute("""INSERT INTO user_info (name, email, phone_no, password) VALUES (%s, %s, %s, %s)""",
                       (name, email, ph_no, password))
        mysql.connection.commit()
        return index()


def index():
    """it gives the entire data from the emp table in crud database
    and returned that data to index.html file to display"""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM user_info ORDER BY id")
    employee = cur.fetchall()
    return render_template('index.html', employee=employee)


@app.route("/ajax_add", methods=["POST", "GET"])
def ajax_add():
    """get the user entered details from the form and add
     those details to the database """
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    # getting user entered details using the name attribute from the form
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        pwd = request.form['pwd']
        # If the form details are empty show the error message
        if name == '':
            msg = "Please Input Name"
        elif email == '':
            msg = "Please Input Email ID"
        elif phone == '':
            msg = "Please Input Phone Number"
        elif pwd == '':
            msg = "Please Input Password"
        else:
            cur.execute("""SELECT * FROM user_info WHERE email LIKE %s""", [email])
            record = cur.fetchall()
            print(record)
            if len(record) > 0:
                msg = """<span style="color:red;">Email is already exists. Create account using another email.</span>"""
            else:
                cur.execute("""INSERT INTO user_info (name, email, phone_no, password) VALUES (%s, %s, %s, %s)""",
                            (name, email, phone, pwd))
                mysql.connection.commit()
                cur.close()
                msg = "New record is created successfully."
    return jsonify(msg)


@app.route("/ajax_update", methods=["POST", "GET"])
def ajax_update():
    """user can edit the existed details from the database"""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        pwd = request.form['pwd']
        print("String is: " + str(string))
        cur.execute("UPDATE user_info SET name = %s, email = %s, phone_no = %s, password = %s WHERE id = %s ",
                    [name, email, phone, pwd, string])
        mysql.connection.commit()
        cur.close()
        msg = "Record is Successfully Updated."
    return jsonify(msg)    


@app.route("/ajax_delete", methods=["POST", "GET"])
def ajax_delete():
    """this method is for delete the particular row from the database"""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        id = request.form['string']
        print(id)
        cur.execute("""DELETE FROM user_info WHERE id = (%s)""", [id])
        mysql.connection.commit()       
        cur.close()
        msg = "Record is Deleted Successfully."
    return jsonify(msg) 
 

app.run(debug=True)
