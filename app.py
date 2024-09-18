from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import google.generativeai as genai
import os
from pdf2image import convert_from_path
from PIL import Image
import pytesseract

app = Flask(__name__)
CORS(app)

api_key = "AIzaSyCaWtf_lQLw9D3aE--GGZwkunDLzF8D4Bc"
genai.configure(api_key=api_key)

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

@app.route('/argument-predict', methods=['POST'])
def argument_predict():
    data = request.json
    user_input = data.get('userMessage')

    try:
        model = genai.GenerativeModel("gemini-1.5-pro")
        prompt = ("Here's some description of a case, can you please tell, what arguments can be made from both sides? And how likely is the user to win (like an approximate percentage) ?")

        response = model.generate_content([prompt, user_input])
        result = response.text

        return jsonify({'analysis': result})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)})

@app.route('/upload-document', methods=['POST'])
def upload_document():
    try:
        # Check if a file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']

        image_dir = "uploads/images"
        if not os.path.exists(image_dir):
            os.makedirs(image_dir)

        # Save the uploaded file temporarily
        file_path = os.path.join("uploads", file.filename)
        file.save(file_path)

        print(f"Processing PDF: {file_path}")
        
        # Convert PDF to images (for multi-page PDFs)
        images = convert_from_path(file_path, poppler_path="C:/Users/Aditi/OneDrive/Desktop/poppler-24.07.0/Library/bin")  # Update path as necessary

        print(f"Number of pages: {len(images)}")
        
        # Initialize text container for all pages
        extracted_text = ""

        # Extract text from each image
        for i, image in enumerate(images):
            image_path = os.path.join(image_dir, f"page_{i+1}.png")
            print(f"Saving page {i+1} to {image_dir}")
            image.save(image_path, "PNG")  # Save the image to the specific folder
            text = pytesseract.image_to_string(image)  # Extract text via OCR
            extracted_text += text

        # Clean up: delete the temporary file
        os.remove(file_path)

        # Send extracted text to the Gemini API for summarization
        model = genai.GenerativeModel("gemini-1.5-flash")
        prompt = "Here is the text of a legal document. Please summarize it for me."
        response = model.generate_content([prompt, extracted_text])
        summary = response.text

        return jsonify({'summary': summary})

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
