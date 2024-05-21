# Doing library imports from Transformers and Flask
from flask import Flask, render_template, request, jsonify
from transformers import AutoTokenizer, TFAutoModelForSequenceClassification
import tensorflow as tf

# Initializing Flask app
app = Flask(__name__)

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

# route for home page
@app.route('/')
def home():
    return render_template('home.html')

# handing the analysis request sent by user
@app.route('/analyze', methods=['POST'])
def handle():
    text = request.form['text']
    sentiment = analyze(text)
    return jsonify({'text': text, 'sentiment': sentiment})

# running Flask app
if __name__ == "__main__":
    app.run(debug= True)