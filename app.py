from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Frontend aur backend connect karne ke liye

# API Key ko securely load karna
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("API key not found! Set GEMINI_API_KEY in Railway Variables.")

genai.configure(api_key=API_KEY)

@app.route("/")
def index():
    return render_template("index.html")  # Frontend page load karega

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(user_message)
        return jsonify({"reply": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway needs this!
    app.run(host="0.0.0.0", port=port)
