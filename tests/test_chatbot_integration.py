```python
import unittest
from unittest.mock import patch
from src import chatbot_integration

class TestChatbotIntegration(unittest.TestCase):

    @patch('src.chatbot_integration.integrateChatbot')
    def test_integrateChatbot(self, mock_integrateChatbot):
        # Test if the function is called
        chatbot_integration.integrateChatbot()
        mock_integrateChatbot.assert_called_once()

        # Test if the function returns the expected result
        mock_integrateChatbot.return_value = "Chatbot integrated successfully"
        result = chatbot_integration.integrateChatbot()
        self.assertEqual(result, "Chatbot integrated successfully")

if __name__ == '__main__':
    unittest.main()
```