from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
import axios
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

GEMINI_API_URL = 'https://api.gemini.com/v1/argument-prediction'
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

@app.route('/api/argument-prediction', methods=['POST'])
def argument_prediction():
    try:
        data = request.json
        description = data.get('description', '')

        if not description:
            return jsonify({'result': 'Please provide a case description.'}), 400

        headers = {
            'Authorization': f'Bearer {GEMINI_API_KEY}',
            'Content-Type': 'application/json'
        }
        payload = {'description': description}

        response = requests.post(GEMINI_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json()
        return jsonify({'result': result.get('arguments', 'No arguments found.')})
    except Exception as e:
        return jsonify({'result': f'Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
