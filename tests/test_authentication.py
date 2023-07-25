```python
import unittest
from src.authentication import authenticateUser

class TestAuthentication(unittest.TestCase):

    def setUp(self):
        self.valid_credentials = {
            'username': 'test_user',
            'password': 'test_password'
        }
        self.invalid_credentials = {
            'username': 'invalid_user',
            'password': 'invalid_password'
        }

    def test_authenticate_user_valid_credentials(self):
        result = authenticateUser(self.valid_credentials['username'], self.valid_credentials['password'])
        self.assertEqual(result, True)

    def test_authenticate_user_invalid_credentials(self):
        result = authenticateUser(self.invalid_credentials['username'], self.invalid_credentials['password'])
        self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()
```