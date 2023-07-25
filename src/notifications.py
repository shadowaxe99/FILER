```python
import os
from twilio.rest import Client

# Twilio API credentials
TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_notification(to, message):
    """
    Function to send SMS notifications using Twilio API
    :param to: Recipient phone number
    :param message: Message content
    :return: None
    """
    try:
        message = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=to
        )
        print(f'Successfully sent message: {message.sid}')
    except Exception as e:
        print(f'Failed to send message: {str(e)}')
```