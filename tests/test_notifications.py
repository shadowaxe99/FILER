```python
import unittest
from unittest.mock import patch
from src.notifications import sendNotification

class TestNotifications(unittest.TestCase):

    @patch('src.notifications.TwilioClient')
    def test_send_notification(self, MockTwilioClient):
        # Arrange
        mock_client = MockTwilioClient.return_value
        mock_client.send_message.return_value = True
        recipient = '1234567890'
        message = 'Test message'

        # Act
        result = sendNotification(recipient, message)

        # Assert
        self.assertTrue(result)
        mock_client.send_message.assert_called_once_with(recipient, message)

if __name__ == '__main__':
    unittest.main()
```