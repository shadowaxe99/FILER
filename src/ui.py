```python
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
from src.chatbot_integration import integrateChatbot
from src.response_generation import generateResponse

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle("AI Chatbot Assistant")
        self.setGeometry(100, 100, 800, 600)

        self.chatWindow = QTextEdit(self)
        self.chatWindow.setReadOnly(True)

        self.responseInput = QTextEdit(self)
        self.sendButton = QPushButton("Send", self)
        self.sendButton.clicked.connect(self.sendResponse)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.chatWindow)
        self.layout.addWidget(self.responseInput)
        self.layout.addWidget(self.sendButton)

        self.container = QWidget()
        self.container.setLayout(self.layout)

        self.setCentralWidget(self.container)

    def sendResponse(self):
        user_message = self.responseInput.toPlainText()
        self.chatWindow.append("User: " + user_message)
        self.responseInput.clear()

        chatbot_response = generateResponse(user_message)
        self.chatWindow.append("AI Chatbot Assistant: " + chatbot_response)

    def incomingMessage(self, message):
        self.chatWindow.append("Incoming: " + message)
        chatbot_response = generateResponse(message)
        self.chatWindow.append("AI Chatbot Assistant: " + chatbot_response)

def renderUI():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    renderUI()
```