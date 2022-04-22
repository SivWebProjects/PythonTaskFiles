from flask import Flask, render_template, url_for, request, json, jsonify
from flaskext.mysql import MySQL
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'flaskapp'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


@app.route('/')
def home():
    return render_template('signup_user_flask.html')


@app.route('/signup', methods=['POST'])
def signup():
    """
    Insert user details into the table if the user doesn't register before
    and enter all the fields else return already registered
    """
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _pwd = _json['password']

    if _email and _name and _pwd:
        cursor.execute('SELECT email FROM user_test_flask WHERE email = %s', (_email))
        user_exist = cursor.fetchone()
        if user_exist:
            resp = jsonify({'message': 'User already registered'})
            resp.status_code = 409
            return resp
        else:
            sql = "INSERT INTO user_test_flask(name, email, pwd) VALUES(%s, %s, %s)"
            data = (_name, _email, generate_password_hash(_pwd),)
            cursor.execute(sql, data)
            conn.commit()
            cursor.close()
            conn.close()

            resp = jsonify({'message': 'User registered successfully'})
            resp.status_code = 201
            return resp
    else:
        resp = jsonify({'message': 'Bad Request - invalid parameters'})
        resp.status_code = 400
        return resp


app.run(debug=True)
