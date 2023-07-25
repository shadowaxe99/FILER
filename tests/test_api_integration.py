```python
import unittest
from unittest.mock import patch
from src import api_integration

class TestAPIIntegration(unittest.TestCase):

    @patch('src.api_integration.requests')
    def test_handleAPIRequest(self, mock_requests):
        # Mocking the API response
        mock_requests.get.return_value.status_code = 200
        mock_requests.get.return_value.json.return_value = {"message": "success"}

        response = api_integration.handleAPIRequest('GET', 'https://api.example.com')

        # Assert the request was of correct type and made to correct url
        mock_requests.get.assert_called_with('https://api.example.com')

        # Assert the response was as expected
        self.assertEqual(response, {"message": "success"})

    @patch('src.api_integration.requests')
    def test_handleAPIRequest_failure(self, mock_requests):
        # Mocking the API response
        mock_requests.get.return_value.status_code = 404

        response = api_integration.handleAPIRequest('GET', 'https://api.example.com')

        # Assert the request was of correct type and made to correct url
        mock_requests.get.assert_called_with('https://api.example.com')

        # Assert the response was as expected
        self.assertEqual(response, None)

if __name__ == '__main__':
    unittest.main()
```