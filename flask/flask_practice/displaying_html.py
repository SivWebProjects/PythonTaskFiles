from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('dis_html_home.html', content ="Flask")


@app.route('/index')
def index():
    return render_template('dis_html_index.html', content=['HTML', 'CSS', 'JavaScript'])


app.run(debug = True)