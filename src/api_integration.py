```python
import requests
from src.config import API_KEYS

def handleAPIRequest(url, method, data=None, headers=None):
    """
    Function to handle API requests
    """
    if method == 'GET':
        response = requests.get(url, headers=headers)
    elif method == 'POST':
        response = requests.post(url, json=data, headers=headers)
    elif method == 'PUT':
        response = requests.put(url, json=data, headers=headers)
    elif method == 'DELETE':
        response = requests.delete(url, headers=headers)
    else:
        raise ValueError(f'Invalid method: {method}')

    response.raise_for_status()

    return response.json()

def integrateChatbot(chatbot_platform):
    """
    Function to integrate with chatbot platforms
    """
    if chatbot_platform == 'Dialogflow':
        url = 'https://api.dialogflow.com/v1/query?v=20150910'
        headers = {'Authorization': f'Bearer {API_KEYS["Dialogflow"]}'}
    elif chatbot_platform == 'Rasa':
        url = 'http://localhost:5005/webhooks/rest/webhook'
    elif chatbot_platform == 'Microsoft Bot Framework':
        url = 'https://directline.botframework.com/v3/directline/conversations'
        headers = {'Authorization': f'Bearer {API_KEYS["Microsoft Bot Framework"]}'}
    else:
        raise ValueError(f'Invalid chatbot platform: {chatbot_platform}')

    return url, headers
```