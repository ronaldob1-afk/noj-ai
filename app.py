from flask import Flask, request, jsonify
import openai, os

# OpenAI API key (set in Render environment)
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/noj", methods=["POST"])
def noj():
    data = request.get_json() or {}
    user_input = data.get("text", "")

    prompt = (
        "You are N.O.J. (Naldo’s Own Jarvis), a loyal, confident, and witty AI assistant."
        f"\n\nUser says: {user_input}"
    )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-5",
            messages=[{"role": "system", "content": prompt}]
        )
        reply = response.choices[0].message["content"]
    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"reply": reply})

# Optional home route for quick Render test
@app.route("/", methods=["GET"])
def home():
    return "N.O.J. is live at https://noj-ai.onrender.com 🚀"

if __name__ == "__main__":
    port = int(os.getenv("PORT", 10000))
    app.run(host="0.0.0.0", port=port)