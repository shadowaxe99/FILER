```python
import tensorflow as tf
from tensorflow.keras.models import load_model
from src.utils import preprocess_text
from src.constants import NLP_MODEL

def load_nlp_model(model_path):
    """
    Load the NLP model from the specified path
    """
    global NLP_MODEL
    NLP_MODEL = load_model(model_path)

def generate_response(input_text):
    """
    Generate a response to the input text using the NLP model
    """
    # Preprocess the input text
    input_text = preprocess_text(input_text)

    # Predict the response using the NLP model
    response = NLP_MODEL.predict([input_text])

    return response
```