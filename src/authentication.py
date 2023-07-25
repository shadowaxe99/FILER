```python
import jwt
from datetime import datetime, timedelta
from src.config import getConfig

SECRET_KEY = getConfig('SECRET_KEY')

def authenticateUser(username, password):
    """
    Function to authenticate user. In real-world applications, you would check these credentials against a database.
    """
    if username == 'admin' and password == 'password':  # Replace with real authentication logic
        return generateToken(username)
    else:
        return None

def generateToken(username):
    """
    Function to generate JWT token
    """
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': username
    }
    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm='HS256'
    )

def decodeToken(token):
    """
    Function to decode JWT token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY)
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
```