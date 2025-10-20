import requests

# N.O.J. URL — your Render link
url = "https://noj-ai.onrender.com/noj"

# What you want to ask N.O.J.
data = {"text": "Hi N.O.J., tell me a joke!"}

# Send POST request to N.O.J.
response = requests.post(url, json=data)

# Print only N.O.J.'s reply
print(response.json()["reply"])
