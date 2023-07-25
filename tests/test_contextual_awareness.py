```python
import unittest
from unittest.mock import patch
from src.contextual_awareness import maintainContext

class TestContextualAwareness(unittest.TestCase):

    @patch('src.contextual_awareness.NLP_MODEL')
    def test_maintainContext(self, mock_model):
        # Mocking the NLP model's response
        mock_model.return_value = "Sure, I can help with that."

        # Test case: User asks a follow-up question
        context = {"previous_messages": ["What's the weather like?", "It's sunny."]}
        message = "What about tomorrow?"
        expected_response = "Sure, I can help with that."
        
        actual_response = maintainContext(message, context)
        self.assertEqual(actual_response, expected_response)

        # Test case: User starts a new conversation
        context = {"previous_messages": ["What's the weather like?", "It's sunny."]}
        message = "Can you set a reminder for me?"
        expected_response = "Sure, I can help with that."
        
        actual_response = maintainContext(message, context)
        self.assertEqual(actual_response, expected_response)

if __name__ == '__main__':
    unittest.main()
```