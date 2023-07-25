```python
import os
import docker

def deployApplication():
    client = docker.from_env()

    # Build Docker image
    print("Building Docker image...")
    client.images.build(path=".", tag="ai_chatbot_assistant")

    # Run Docker container
    print("Running Docker container...")
    container = client.containers.run("ai_chatbot_assistant", detach=True, ports={'5000/tcp': 5000})

    print(f"AI Chatbot Assistant is running in Docker container with ID: {container.id}")

if __name__ == "__main__":
    deployApplication()
```