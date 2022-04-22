from flask import Flask, render_template, request, jsonify
import sqlite3 as sql

app = Flask(__name__)

conn = sql.connect('login_db.db')
conn.cursor()


@app.route('/')
def home():
    """Displays home page which contains links for register and login pages."""
    return render_template('home_page.html')


@app.route('/register')
def register():
    """Displays register page which takes the user details and stores into the database."""
    return render_template('registration_page.html')


@app.route('/login')
def login():
    """Displays login page which takes username and password for authentication."""
    return render_template('login_page.html')


@app.route('/add', methods=['POST'])
def add():
    """If details are stored in the table success message is displayed else error message is displayed."""
    if request.method == 'POST':
        try:
            user_name = request.form['user_name']
            email = request.form['email']
            contact = request.form['ph_no']
            password = request.form['password']

            with sql.connect('login_db.db') as con:
                cur = con.cursor()
                cur.execute("INSERT INTO user_details(user_name, email, phone_no, password) VALUES (?, ?, ?, ?)",
                            (user_name, email, contact, password))
                msg = "Successfully added details into the database."
                con.close()
        except:
            con.rollback()
            con.close()
            msg = "Error..! couldn't insert the details into the database."
        finally:
            return render_template("result.html", msg=msg)


@app.route('/check', methods=['POST'])
def check():
    """If login credentials are existed in the table their details will be displayed
    else registration form is displayed."""
    user_name = request.form['user_name']
    password = request.form['password']

    with sql.connect('login_db.db') as con:
        cur = con.cursor()
        row = cur.execute(f"SELECT * FROM user_details WHERE user_name='{user_name}' AND password='{password}';")
        if not row.fetchone():
            print("Empty Row")
            return render_template('registration_page.html')
        else:
            print("Row is fetched: " + str(row))
            user_details = cur.execute(f"SELECT * FROM user_details WHERE user_name='{user_name}'")
            return render_template("success_page.html", user_details=user_details)
        con.close()


app.run(debug=True)
