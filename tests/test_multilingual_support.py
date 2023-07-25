```python
import unittest
from src.multilingual_support import translateMessage

class TestMultilingualSupport(unittest.TestCase):

    def setUp(self):
        self.message = "Hello, how are you?"
        self.target_language = "es"

    def test_translateMessage(self):
        translated_message = translateMessage(self.message, self.target_language)
        self.assertIsNotNone(translated_message)
        self.assertIsInstance(translated_message, str)

    def test_translateMessage_invalid_language(self):
        with self.assertRaises(ValueError):
            translateMessage(self.message, "invalid_language")

if __name__ == "__main__":
    unittest.main()
```