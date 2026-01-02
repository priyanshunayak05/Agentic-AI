import fitz  # PyMuPDF

def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a StreamlitUploadedFile (PDF).
    """
    try:
        # Read the file bytes
        bytes_data = uploaded_file.read()
        
        # Open with fitz
        doc = fitz.open(stream=bytes_data, filetype="pdf")
        
        text = ""
        for page in doc:
            text += page.get_text()
            
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"
