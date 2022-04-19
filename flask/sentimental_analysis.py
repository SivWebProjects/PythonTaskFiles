from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def emotion_score(sentence):
    """
    Receives user text as an input and returns emotion and score.
    
        Parameters:
            sentence (str): text
        
        Return type:
            sentence (str): emotion and score
    """
    # Creating a SentimentIntensityAnalyzer object.
    sia_obj = SentimentIntensityAnalyzer()

    # sentiment dictionary contains 4 classes of sentiments which are:
    # neg: Negative, neu: Neutral, pos: Positive
    # and compound: Compound (i.e. aggregated score)
    sentiment_dict = sia_obj.polarity_scores(sentence)
    print(sentiment_dict)

    emotion = ""

    # decides sentiment as positive, negative and neutral based on the compound value
    if sentiment_dict['compound'] >= 0.05:
        emotion = "Positive"

    elif sentiment_dict['compound'] <= -0.05:
        emotion = "negative"

    else:
        emotion = "neutral"

    message = emotion + " " + str(sentiment_dict['compound'])

    return message


app = Flask(__name__)


@app.route('/')
def home():
    """This displays the code written in html file."""

    return render_template('home3.html')


@app.route('/text', methods=['GET', 'POST'])
def text():
    """The user entered text is received when the user clicks on the submit button
    and stores in the text variable and the value in the variable is passed as an 
    argument to the emotion_score() function and this function returns emotion and score value.

    Parameters:
        None: no arguments
        
    Return type:
        sentiment (str): emotion and score
    """
    # In form[text] text is the value of the name attribute of an input text element
    text = request.form['text']
    sentiment = emotion_score(text)

    return sentiment


app.run(debug=True)
