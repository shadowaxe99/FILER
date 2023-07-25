```python
import unittest
from unittest.mock import patch
from src import ui

class TestUI(unittest.TestCase):

    @patch('src.ui.renderUI')
    def test_renderUI(self, mock_renderUI):
        # Test if the renderUI function is called when the UI is initialized
        ui.initialize()
        mock_renderUI.assert_called_once()

    @patch('src.ui.updateUI')
    def test_updateUI(self, mock_updateUI):
        # Test if the updateUI function is called when a new message is received
        ui.newMessageReceived()
        mock_updateUI.assert_called_once()

    @patch('src.ui.displayError')
    def test_displayError(self, mock_displayError):
        # Test if the displayError function is called when an error occurs
        ui.errorOccurred()
        mock_displayError.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```