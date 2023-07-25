```python
import unittest
from src.database import storeData, DB_CONNECTION

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db_connection = DB_CONNECTION
        self.test_data = {
            "user_id": "123",
            "preferences": {
                "language": "English",
                "tone": "formal"
            }
        }

    def test_storeData(self):
        result = storeData(self.test_data)
        self.assertTrue(result)

    def test_database_connection(self):
        self.assertIsNotNone(self.db_connection)

if __name__ == '__main__':
    unittest.main()
```