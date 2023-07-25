```python
import sqlite3
from sqlite3 import Error
from src.config import getConfig

# Database configuration
DB_CONFIG = getConfig('DATABASE')

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(DB_CONFIG['DB_FILE'])
        print(f'Successful SQLite connection with {DB_CONFIG["DB_FILE"]}')
    except Error as e:
        print(e)
    return conn

def close_connection(conn):
    conn.close()

def execute_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
    except Error as e:
        print(e)

def storeData(user_preferences, chat_message, chat_response):
    conn = create_connection()

    user_preferences_query = f"""
    INSERT INTO UserPreferences(id, preferences)
    VALUES({user_preferences['id']}, {user_preferences['preferences']})
    """

    chat_message_query = f"""
    INSERT INTO ChatMessage(id, sender, content, timestamp)
    VALUES({chat_message['id']}, {chat_message['sender']}, {chat_message['content']}, {chat_message['timestamp']})
    """

    chat_response_query = f"""
    INSERT INTO ChatResponse(id, content, timestamp)
    VALUES({chat_response['id']}, {chat_response['content']}, {chat_response['timestamp']})
    """

    execute_query(conn, user_preferences_query)
    execute_query(conn, chat_message_query)
    execute_query(conn, chat_response_query)

    close_connection(conn)
```