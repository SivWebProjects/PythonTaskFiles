from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        todo = request.form.get("todo")
        print(todo)
    return render_template('home.html')


app.run(debug=True)
