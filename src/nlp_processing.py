```python
import tensorflow as tf
from tensorflow.keras.models import load_model
from nltk.tokenize import word_tokenize
from src.utils import utilFunction

class NLPProcessor:
    def __init__(self):
        self.model = load_model('path_to_model')

    def preprocess_text(self, text):
        # Tokenize the text
        tokenized_text = word_tokenize(text)
        return tokenized_text

    def generate_response(self, tokenized_text):
        # Convert tokenized text to tensor for prediction
        input_tensor = tf.convert_to_tensor(tokenized_text)
        input_tensor = tf.expand_dims(input_tensor, 0)

        # Predict the response
        prediction = self.model.predict(input_tensor)
        predicted_text = utilFunction(prediction)

        return predicted_text

nlp_processor = NLPProcessor()

def generateResponse(text):
    tokenized_text = nlp_processor.preprocess_text(text)
    response = nlp_processor.generate_response(tokenized_text)
    return response
```