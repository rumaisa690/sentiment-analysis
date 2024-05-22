# sentiment-analysis

## Project Overview
This web application does sentiment analysis on user input text, classifying it as positive or negative. It uses Hugging Face's Transformers library with a pre-trained DistilBERT model and TensorFlow for the backend, and Flask to serve the application. The frontend is built using HTML, CSS, and JavaScript.
The first section runs sentiment analysis on user-inputted text.
The second section takes a user-inputted keyword, randomly generates a tweet from the Twitter API, displays the tweet and runs sentiment analysis on it.

I have worked on this project throughout this past semester and only just moved it over to this github account so that's why the repo looks recently created

## Installation

### Prerequisites

- Python 3.7 or higher
- Pip (Python package installer)

### Setup

1. **Cloning the repository**:

    ```sh
    git clone https://github.com/yourusername/sentiment-analysis-app.git
    cd sentiment-analysis-app
    ```

2. **Create a virtual environment** (optional but recommended):

    ```sh
    python -m venv app
    source app/bin/activate  # On Windows use `.\app\Scripts\activate`
    ```

3. **Install the dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Download the pre-trained model**:

    ```sh
    python download_model.py
    ```

5. **Run the Flask app**:

    ```sh
    python app.py
    ```

6. **Open your browser** and go to `http://127.0.0.1:5000/`.

** (Optional after step 4) If you want the tweet sentiment analysis functionality: **

1. Sign up for the Twitter API using the instructions here: https://developer.x.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api
2. Go to the sentiment_app.py file and fill in with API Key, API Key Secret, Access Token, and Token Secret values from your personal account
3. Continue with step 5 and 6 above

## Usage

First Section
1. Enter text in the input box
2. Click the "Analyze" button
3. The sentiment result (Positive or Negative) will be displayed

Second Section
1. Enter a keyword into the input box
2. Click on the "Generate Tweet" button
3. The generated tweet based on the input keyword will be displayed
4. The sentiment result (Positive or Negative) will be displayed

## Project Structure
sentiment_app.py: Main Flask application file that handles routing and sentiment analysis
templates/home.html: HTML file that defines the structure of the web application's frontend and includes JavaScript to handle form submissions and dynamic content updates
static/style.css: CSS file for styling the web application's frontend
model: Directory containing the pre-trained DistilBERT model for sentiment analysis

## Explanation of the Sentiment Analysis Process

1. **Text Extraction**:
   When the user submits the form, the input text is sent to the Flask backend by an HTTP POST request

2. **Text Processing**:
   The backend uses Hugging Face's Transformers library to tokenize the input text and create tensor inputs

3. **Model Prediction**:
   The pre-trained DistilBERT model which is fine-tuned on sentiment analysis, processes the inputs and produces sentiment scores

4. **Sentiment Classification**:
   Based on the model's output, the sentiment is classified as Positive or Negative

5. **Result Display**:
   The backend sends the sentiment result back to the frontend, where it's displayed to the user

## Technologies Used

- **Backend**: Python, Flask, TensorFlow, Transformers (Hugging Face)
- **Frontend**: HTML, CSS, JavaScript
