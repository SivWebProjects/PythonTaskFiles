import re
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pandas as pd
import joblib


def text_clean(dataset):
    """
    Remove characters in words except alphabets and stopword are removed which doesn't have importance.

        Parameters:
           dataset (pd): A dataframe consists of two columns review and label
        Return:
            corpus (list): List consists of words
    """
    corpus = []
    for i in range(len(dataset)):
        review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
        review = review.lower()
        review = review.split()

        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')

        # Creating WordNetLemmatizer object
        lm = WordNetLemmatizer()
        review = [lm.lemmatize(word) for word in review if word not in set(all_stopwords)]
        review = ' '.join(review)
        corpus.append(review)
    return corpus


# Importing dataset
dataset = pd.read_csv('/home/neosoft/Documents/CSVFiles/restaurant_reviews.txt', delimiter=";",
                      names=['Review', 'Label'])
dataset.head(5)
dataset['Label'].replace({"surprise": 1, "love": 1, "joy": 1, "fear": 0, "anger": 0, "sadness": 0}, inplace=True)
corpus = text_clean(dataset)

cv = CountVectorizer(max_features=1500)
x = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, -1].values

# Splitting dataset into training and testing set
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)

# Training the Random Forest Model
rf_model = RandomForestClassifier(n_estimators=501, criterion='entropy')
rf_model.fit(x_train, y_train)

# Predicting test results
y_pred = rf_model.predict(x_test)

score = accuracy_score(y_test, y_pred)
print(score)

# Saving the model for further use
joblib.dump(rf_model, 'rf_model_jlib')


# DThe function for input text preprocessing
def text_to_array(input_text):
    """
    Remove characters in given words except alphabets and stopword are removed.

        Parameters:
           input_text (str): Text
        Return:
            corpus (list): A List
    """
    corpus = []
    text = re.sub('[^a-zA-Z]', ' ', input_text)
    text = text.lower()
    text = text.split()

    all_stopwords = stopwords.words('english')
    all_stopwords.remove('not')

    lm = WordNetLemmatizer()
    text = [lm.lemmatize(word) for word in text if word not in set(all_stopwords)]
    text = ' '.join(text)
    corpus.append(text)
    text_to_array = cv.transform(corpus).toarray()
    return text_to_array
