import requests

# Replace with your Render URL
url = "https://noj-ai.onrender.com/noj"

data = {"text": "Hi N.O.J., tell me a joke!"}

response = requests.post(url, json=data)
print(response.json()["reply"])