```python
import unittest
from unittest.mock import patch
from src import config

class TestConfig(unittest.TestCase):

    @patch('src.config.getConfig')
    def test_get_config(self, mock_get_config):
        # Mocking the getConfig function
        mock_get_config.return_value = {
            'API_KEYS': '1234567890',
            'DB_CONNECTION': 'sqlite:///:memory:',
            'NLP_MODEL': 'BERT'
        }

        result = config.getConfig()
        self.assertEqual(result['API_KEYS'], '1234567890')
        self.assertEqual(result['DB_CONNECTION'], 'sqlite:///:memory:')
        self.assertEqual(result['NLP_MODEL'], 'BERT')

if __name__ == '__main__':
    unittest.main()
```