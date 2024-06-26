# Doing library imports from Transformers and Flask
from flask import Flask, render_template, request, jsonify
import tweepy
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf
import random

# Initializing Flask app
app = Flask(__name__)

# Authenticate with Twitter API using your credentials
API_KEY = "" ## Fill with your API Key
API_SECRET_KEY = "" ## Fill with your API Key Secret
ACCESS_TOKEN = "" ## Fill with your Access Token
ACCESS_TOKEN_SECRET = "" ## Fill with your Token Secret

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Loading the pre-traned model & tokenizer from directory
name = 'distilbert-base-uncased-finetuned-sst-2-english'
model = TFAutoModelForSequenceClassification.from_pretrained('./model')
tokenizer = AutoTokenizer.from_pretrained('./model')

# Analyzing the sentiment of input user text
def analyze(text):
    # tokenizing input text
    tokens = tokenizer(text, return_tensors="tf", truncation= True, padding= True, max_length= 512)
    outputs = model(tokens)

    # using softmax to get probabilities
    probs = tf.nn.softmax(outputs.logits, axis = -1)

    # getting positive & negative scores
    positive = probs[0][1].numpy()
    negative = probs[0][0].numpy()

    # returning the calculated sentiment
    return "Positive" if positive > negative else "Negative"

def fetch_tweet(keyword):
    tweets = api.search_tweets(q = keyword, lang = "en", count = 100)
    if tweets:
        print("tweet:", random.choice(tweets).text)
        return random.choice(tweets).text
    else:
        return "No tweet found"

# route for home page
@app.route('/')
def home():
    return render_template('home.html')

# handing the analysis request sent by user
@app.route('/analyze', methods= ['POST'])
def handle():
    text = request.form['text']
    sentiment = analyze(text)

    return jsonify({'text': text, 'sentiment': sentiment})

# fetching a tweet based on the user's specified keyword
@app.route('/fetch_tweet', methods= ['POST'])
def tweet_sentiment():
    keyword = request.form['keyword']
    print("keyword", keyword)
    tweet = fetch_tweet(keyword)
    sentiment = analyze(tweet)

    return jsonify({'text': tweet, 'sentiment': sentiment})


# running Flask app
if __name__ == "__main__":
    app.run(debug= True)