from flask import Flask, render_template, request
# To import the model which was built and saved
import joblib
# In trained module text_to_array is a function for text preprocessing
from trained_model import text_to_array

app = Flask(__name__)


@app.route('/')
def home():
    """Display home page where user enter text to find emotion."""
    return render_template('home.html')


@app.route('/text', methods=['GET', 'POST'])
def text():
    """
    Receives user text as an input and returns emotion and score.

        Return type:
            message (str): emotion and score
    """
    text = request.form['text']
    input_text_array = text_to_array(text)

    # Loading the model that was built and saved as model_jlib
    model = joblib.load('rf_model_jlib')

    text_class = model.predict(input_text_array)
    if text_class == 0:
        msg = "Negative"
    else:
        msg = "Positive"
    score = max(model.predict_proba(input_text_array)[0])
    message = msg + " " + str(score)
    # message = """<h3 style="color:blue;">msg=%s: + <span style="color:yellow;">
    # score=%s</span></h3>""", (msg, str(score))
    print(message)
    return message


app.run(debug=True)
