# sentiment-analysis

## Project Overview
This web application does sentiment analysis on user input text, classifying it as positive or negative. It uses Hugging Face's Transformers library with a pre-trained DistilBERT model and TensorFlow for the backend, and Flask to serve the application. The frontend is built using HTML, CSS, and JavaScript.

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
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
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

## Usage

1. Enter text in the input box on the web page.
2. Click the "Analyze" button.
3. The sentiment result (Positive or Negative) will be displayed on the page.

## Project Structure

## Explanation of the Sentiment Analysis Process

1. **Text Extraction**:
   When the user submits the form, the input text is sent to the Flask backend by an HTTP POST request.

2. **Text Processing**:
   The backend uses Hugging Face's Transformers library to tokenize the input text and create tensor inputs.

3. **Model Prediction**:
   The pre-trained DistilBERT model which is fine-tuned on sentiment analysis, processes the inputs and produces sentiment scores.

4. **Sentiment Classification**:
   Based on the model's output, the sentiment is classified as Positive or Negative.

5. **Result Display**:
   The backend sends the sentiment result back to the frontend, where it's displayed to the user.

## Technologies Used

- **Backend**: Python, Flask, TensorFlow, Transformers (Hugging Face)
- **Frontend**: HTML, CSS, JavaScript
