from flask import Flask, request, jsonify
import pytesseract
import cv2
import numpy as np
from pdf2image import convert_from_bytes

app = Flask(__name__)

@app.route('/extract-text', methods=['POST'])
def extract_text():
    file = request.files['file']
    images = convert_from_bytes(file.read())
    text_data = []
    
    for img in images:
        img_np = np.array(img)
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(gray)
        text_data.append(text)
    
    return jsonify({'text': text_data})

if __name__ == '__main__':
    app.run(debug=True)