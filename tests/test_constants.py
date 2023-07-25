```python
import unittest
from src import constants

class TestConstants(unittest.TestCase):

    def test_constants(self):
        self.assertIsNotNone(constants.API_KEYS)
        self.assertIsNotNone(constants.DB_CONNECTION)
        self.assertIsNotNone(constants.NLP_MODEL)

if __name__ == '__main__':
    unittest.main()
```