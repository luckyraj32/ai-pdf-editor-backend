import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AI PDF Editor Backend is running successfully!"})

@app.route("/edit-pdf", methods=["POST"])
def edit_pdf():
    try:
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        pdf_file = request.files["file"]
        edited_pdf_path = "edited_output.pdf"
        pdf_file.save(edited_pdf_path)
        
        return jsonify({"message": "PDF processed successfully", "file_path": edited_pdf_path})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Railway-assigned port
    app.run(host="0.0.0.0", port=port)
