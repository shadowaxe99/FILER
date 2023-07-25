```python
import json
import os

def load_api_keys(file_path):
    """
    Load API keys from a JSON file
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            API_KEYS = json.load(f)
        return API_KEYS
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")

def save_user_preferences(user_preferences, file_path):
    """
    Save user preferences to a JSON file
    """
    with open(file_path, 'w') as f:
        json.dump(user_preferences, f)

def load_user_preferences(file_path):
    """
    Load user preferences from a JSON file
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            user_preferences = json.load(f)
        return user_preferences
    else:
        raise FileNotFoundError(f"{file_path} does not exist.")

def format_chat_message(message):
    """
    Format chat message for display in the UI
    """
    return f"{message['timestamp']}: {message['sender']}: {message['content']}"

def format_chat_response(response):
    """
    Format chatbot response for display in the UI
    """
    return f"{response['timestamp']}: AI Chatbot Assistant: {response['content']}"
```