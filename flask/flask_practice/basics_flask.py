from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Welcome To <span style=color:Red;font-size:30px;>Home Page</span></h1>'

#Dynamic Routing means displaying value in the web page taking from the url 
@app.route("/<name>")
def display_name(name):
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


app.run(debug=True)