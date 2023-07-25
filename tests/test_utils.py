```python
import unittest
from src import utils

class TestUtils(unittest.TestCase):

    def setUp(self):
        self.sample_data = {
            "message": "Hello, how can I assist you?",
            "timestamp": "2022-01-01T00:00:00Z",
            "sender": "AI Chatbot Assistant"
        }

    def test_utilFunction(self):
        result = utils.utilFunction(self.sample_data)
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
```