from transformers import TFAutoModelForSequenceClassification, AutoTokenizer
name = 'distilbert-base-uncased-finetuned-sst-2-english'
model = TFAutoModelForSequenceClassification.from_pretrained(name)
tokenizer = AutoTokenizer.from_pretrained(name)

# saving model & tokenizer locally
model.save_pretrained("./model")
tokenizer.save_pretrained("./model")