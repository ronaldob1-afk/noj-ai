# app.py
from flask import Flask, request, jsonify
import openai, os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/noj", methods=["POST"])
def noj():
    data = request.get_json() or {}
    user_input = data.get("text", "")
    prompt = (
        "You are N.O.J. (Naldo’s Own Jarvis), a loyal, confident, and witty AI assistant."
        f"\n\nUser says: {user_input}"
    )

    response = openai.ChatCompletion.create(
        model="gpt-5",
        messages=[{"role": "system", "content": prompt}]
    )

    reply = response.choices[0].message["content"]
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)))
