from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL, MySQLdb
app = Flask(__name__)
       
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'flaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)


@app.route('/')
def index():
    """Displays records in the table in the ascending order by id."""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM employee ORDER BY id")
    employee = cur.fetchall()
    return render_template('index.html', employee=employee)


@app.route("/ajax_add", methods=["POST", "GET"])
def ajax_add():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    """Insert records in the table when all fields values are provided else error message is displayed."""
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        print(txtname)
        if txtname == '':
            msg = 'Please Input name'  
        elif txtdepartment == '':
           msg = 'Please Input Department'  
        elif txtphone == '':
           msg = 'Please Input Phone'  
        else:        
            cur.execute("INSERT INTO employee (name,department,phone) VALUES (%s,%s,%s)",
                        [txtname, txtdepartment, txtphone])
            mysql.connection.commit()       
            cur.close()
            msg = 'New record created successfully'   
    return jsonify(msg)


@app.route("/ajax_update", methods=["POST", "GET"])
def ajax_update():
    """Update existed values with new values in the table."""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        print(string)
        cur.execute("UPDATE employee SET name = %s, department = %s, phone = %s WHERE id = %s ",
                    [txtname, txtdepartment, txtphone, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'   
    return jsonify(msg)    


@app.route("/ajax_delete", methods=["POST", "GET"])
def ajax_delete():
    """Delete record if the id number is existed in the table."""
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        getid = request.form['string']
        print(getid)
        cur.execute('DELETE FROM employee WHERE id = {0}'.format(getid))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'   
    return jsonify(msg) 
 

app.run(debug=True)
