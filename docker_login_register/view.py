from flask import Flask, render_template, request
import os
import sqlite3 as sql

app = Flask(__name__)

conn = sql.connect('login_db.db')
conn.cursor()


@app.route('/')
def home():
    """Displays login page which takes username and password for authentication."""
    return render_template('login_page.html')


@app.route('/register/')
def register():
    """Displays registration page which takes the user details and stores into the database."""
    return render_template('registration_page.html')


@app.route('/adding_user', methods=['POST'])
def add_user():
    """If details are stored in the table success message is displayed else error message is displayed."""
    if request.method == 'POST':
        # try:
        user_name = request.form['user_name']
        email = request.form['email']
        phone_no = request.form['ph_no']
        password = request.form['password']

        with sql.connect('login_db.db') as con:
            cur = con.cursor()
            record = cur.execute(f"SELECT * FROM user_details WHERE email='{email}';")
            if not record.fetchone():
                cur.execute("INSERT INTO user_details(user_name, email, phone_no, password) VALUES (?, ?, ?, ?)",
                            (user_name, email, phone_no, password))
                row = cur.execute(f"SELECT * FROM user_details WHERE email='{email}';")
                if not row.fetchone():
                    print("Empty Row")
                    msg = "Details are not added into the database. Please register again."
                    return render_template('registration_page.html', msg=msg)
                else:
                    msg = "Successfully added details into the database."
                    user_details = cur.execute(f"SELECT * FROM user_details WHERE email='{email}';")
                    print("Row is fetched: " + str(user_details))
                    return render_template("success_page.html", user_details=user_details, message=msg)
            else:
                msg = "You account is exists. You don't need to register."
                user_details = cur.execute(f"SELECT * FROM user_details WHERE email='{email}';")
                print("Row is fetched: " + str(user_details))
                return render_template("success_page.html", user_details=user_details, msg=msg)
        con.close()


@app.route('/validation', methods=['POST'])
def login_validation():
    """If login credentials are existed in the table their details will be displayed
    else registration form is displayed."""
    email = request.form['email']
    password = request.form['password']

    with sql.connect('login_db.db') as con:
        cur = con.cursor()
        row = cur.execute(f"SELECT * FROM user_details WHERE email='{email}' AND password='{password}';")
        if not row.fetchone():
            print("Empty Row")
            msg = "Your account is not created. Please register using below link."
            return render_template('login_page.html', msg=msg)
        else:
            user_details = cur.execute(f"SELECT * FROM user_details WHERE email='{email}';")
            print("Row is fetched: " + str(user_details))
            return render_template("success_page.html", user_details=user_details)
    con.close()


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
