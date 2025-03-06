from flask import Flask, render_template, request
import google.generativeai as genai  # Gemini API ke liye
import os

app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))  # Gemini API Key environment variable se lo

def get_gemini_response(prompt):
    model = genai.GenerativeModel("gemini-pro")  # Gemini model
    response = model.generate_content(prompt)
    return response.text  # Gemini ka response return karo

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["message"]
    bot_response = get_gemini_response(user_input)
    return {"response": bot_response}

if __name__ == "__main__":
    app.run(debug=True)
