from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome To <span style=color:Red;font-size:30px;>Home Page</span></h1>'


@app.route("/<name>")
def display_name(name):
    """It performs Dynamic Routing which means displaying value in the web page taking from the url"""
    return f"Hello {name}! Welcome to Home Page!!"


@app.route("/match")
def match():
    return "IPL match starts from May 2022"


@app.route("/match_date")
def match_date():
    return redirect('/match')


@app.route("/home_page")
def home_page():
    return redirect(url_for("home"))


# When debug value is True then no need to run flask program again and again when the changes are made to the code.
app.run(debug=True)
