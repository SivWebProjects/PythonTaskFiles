from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def base():
    return render_template('inherit_base.html')

@app.route('/home')
def home():
    return render_template('inherit_home2.html')


app.run(debug = True)