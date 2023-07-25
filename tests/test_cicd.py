```python
import unittest
from unittest.mock import patch
from src import cicd

class TestCICD(unittest.TestCase):

    @patch('src.cicd.runCICD')
    def test_runCICD(self, mock_runCICD):
        # Test if the function is called when the CI/CD pipeline is triggered
        cicd.runCICD()
        mock_runCICD.assert_called_once()

    @patch('src.cicd.runCICD')
    def test_runCICD_return(self, mock_runCICD):
        # Test if the function returns the correct status
        mock_runCICD.return_value = "CI/CD pipeline ran successfully"
        result = cicd.runCICD()
        self.assertEqual(result, "CI/CD pipeline ran successfully")

if __name__ == '__main__':
    unittest.main()
```