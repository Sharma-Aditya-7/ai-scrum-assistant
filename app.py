import openai
from flask import Flask, request, jsonify

app = Flask(__name__)

# Replace with your OpenAI API key
OPENAI_API_KEY = "your-api-key-here"

def get_agile_advice(prompt):
    """Generate Agile-related responses using OpenAI's API."""
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an AI Scrum Assistant."},
            {"role": "user", "content": prompt}
        ],
        api_key=OPENAI_API_KEY
    )
    return response["choices"][0]["message"]["content"]

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    prompt = data.get("prompt", "")
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400
    
    response = get_agile_advice(prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
