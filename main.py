from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


@app.route('/')
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


# Configure the Gemini API
genai.configure(api_key="AIzaSyD9_ES9XMSaVAxYBktLS-vWKN1emJb-nRU")
def generate_text(model_name="gemini-2.0-flash-001", prompt="Welcome message"):
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_query = data.get('query', '')
    
    if not user_query:
        return jsonify({"error": "Query is required"}), 400
    
    try:

        response = generate_text(prompt=user_query)
        print(response)

        
        
        if response is None:
            return jsonify({"error": "An error occurred while processing the request"}), 500
        
        return jsonify({"response": response})
    except Exception as e:
        import traceback
        error_details = traceback.format_exc()
        print(f"Error: {str(e)}\nTraceback: {error_details}")
        return jsonify({"error": f"{str(e)}", "details": error_details}), 500


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
