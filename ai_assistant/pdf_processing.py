import os
import PyMuPDF as fitz  # PyMuPDF

def load_pdfs(pdf_folder):
    """Load and extract text from all PDFs in the given folder."""
    documents = {}
    for filename in os.listdir(pdf_folder):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_folder, filename)
            text = extract_text_from_pdf(file_path)
            documents[filename] = text
    return documents

def extract_text_from_pdf(pdf_path):
    """Extract text from a single PDF file."""
    text = ""
    with fitz.open(pdf_path) as doc:
        for page in doc:
            text += page.get_text("text") + "\n"
    return text