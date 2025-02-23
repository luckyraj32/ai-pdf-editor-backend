from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "AI PDF Editor Backend is running successfully!"})

@app.route("/edit-pdf", methods=["POST"])
def edit_pdf():
    try:
        # Example: Handle PDF file upload
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400
        
        pdf_file = request.files["file"]
        
        # Process the PDF here (Replace this with your actual AI-based editing code)
        edited_pdf_path = "edited_output.pdf"
        
        # Save the processed file (this is just a placeholder)
        pdf_file.save(edited_pdf_path)
        
        return jsonify({"message": "PDF processed successfully", "file_path": edited_pdf_path})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
