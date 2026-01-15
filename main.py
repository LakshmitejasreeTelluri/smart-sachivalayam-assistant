from flask import Flask, request, jsonify, render_template
from google import genai

# Initialize Gemini client
# ⚠️ Replace with your own API key before running
GEMINI_API_KEY="AIzaSyDLVCxo_PlHxadUkKtr53E3VEAmtFdHYcE"
client = genai.Client(api_key="GEMINI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()

        if not data or "message" not in data:
            return jsonify({"error": "Message field is required"}), 400

        prompt = data["message"]

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return jsonify({
            "reply": response.text
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(port=8000, debug=True)