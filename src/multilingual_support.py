```python
from googletrans import Translator

class MultilingualSupport:
    def __init__(self):
        self.translator = Translator()

    def translate_message(self, message, target_language):
        """
        Translate the given message to the target language using Google Translate API.
        """
        translation = self.translator.translate(message, dest=target_language)
        return translation.text

    def detect_language(self, message):
        """
        Detect the language of the given message using Google Translate API.
        """
        detection = self.translator.detect(message)
        return detection.lang
```