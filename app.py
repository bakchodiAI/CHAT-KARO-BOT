from flask import Flask, render_template, request, jsonify
import os
from flask_cors import CORS
import openai  # Ya jo Gemini ka API wrapper use ho raha hai

app = Flask(__name__)
CORS(app)  # Cross-Origin Requests Allow Karega

# Load API Key from environment variables (Render ke liye)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

@app.route("/")
def home():
    return render_template("index.html")  # Ensure karo ki index.html "templates/" folder me ho

@app.route("/chat", methods=["POST"])
def chat():
    try:
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "Message is required!"}), 400

        # Yahan Gemini API call karo
        response = {
            "bot_reply": f"Gemini API ka reply aayega yahan: '{user_message}'"
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Render ke liye Port 10000
    app.run(host="0.0.0.0", port=port, debug=True)
