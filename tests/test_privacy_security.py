```python
import unittest
from src import privacy_security

class TestPrivacySecurity(unittest.TestCase):

    def setUp(self):
        self.privacy_security = privacy_security.PrivacySecurity()

    def test_ensurePrivacy(self):
        result = self.privacy_security.ensurePrivacy("Sensitive data")
        self.assertIsNotNone(result)

    def test_encryptData(self):
        result = self.privacy_security.encryptData("Sensitive data")
        self.assertNotEqual(result, "Sensitive data")

    def test_decryptData(self):
        encrypted_data = self.privacy_security.encryptData("Sensitive data")
        result = self.privacy_security.decryptData(encrypted_data)
        self.assertEqual(result, "Sensitive data")

if __name__ == '__main__':
    unittest.main()
```