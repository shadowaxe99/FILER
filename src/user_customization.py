```python
from src.database import storeData

class UserPreferences:
    def __init__(self):
        self.preferences = {}

    def get_preferences(self, user_id):
        if user_id in self.preferences:
            return self.preferences[user_id]
        else:
            return None

    def set_preferences(self, user_id, preferences):
        self.preferences[user_id] = preferences
        storeData(user_id, preferences)

    def customizeResponse(self, user_id, response):
        preferences = self.get_preferences(user_id)
        if preferences:
            if 'tone' in preferences:
                response = self.apply_tone(response, preferences['tone'])
            if 'style' in preferences:
                response = self.apply_style(response, preferences['style'])
        return response

    def apply_tone(self, response, tone):
        # Apply tone to the response
        # This is a placeholder and should be replaced with actual implementation
        return response

    def apply_style(self, response, style):
        # Apply style to the response
        # This is a placeholder and should be replaced with actual implementation
        return response
```