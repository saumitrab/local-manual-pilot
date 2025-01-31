import pymupdf
import chromadb
from sentence_transformers import SentenceTransformer
import os

# This script extracts text from PDFs, chunks it, generates embeddings, and stores them in ChromaDB.

# Initialize embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
vector_db = chromadb.PersistentClient(path="./vector_store")

# Get list of PDF files from resources/manuals directory
def get_local_pdf_files():
    pdf_files = []
    manual_dir = "../resources/manuals"
    for file in os.listdir(manual_dir):
        if file.endswith(".pdf"):
            pdf_path = os.path.join(manual_dir, file)
            pdf_files.append(open(pdf_path, "rb"))
    return pdf_files


def process_local_manuals():
    """Process PDFs in the local manuals directory."""
    pdf_files = get_local_pdf_files()
    if pdf_files:
        process_pdfs(pdf_files)
        for f in pdf_files:
            f.close()

    return "PDFs processed successfully!"


def process_pdfs(uploaded_files):
    """Extract text from uploaded PDFs and store embeddings in ChromaDB."""
    collection = vector_db.get_or_create_collection("manuals")
    
    for file in uploaded_files:
        text = extract_text(file)
        chunks = chunk_text(text)
        embeddings = embedding_model.encode(chunks)
        
        for i, emb in enumerate(embeddings):
            collection.add(
                ids=[f"{file.name}-{i}"],
                embeddings=[emb.tolist()],
                documents=[chunks[i]]
            )

    return "PDFs processed successfully!"

def extract_text(pdf_file):
    """Extract text from a PDF file using PyMuPDF."""
    doc = pymupdf.open(pdf_file)
    text = "\n".join([page.get_text("text") for page in doc])
    return text

def chunk_text(text, chunk_size=500):
    """Split text into smaller, meaningful chunks."""
    sentences = text.split(". ")
    chunks = []
    chunk = ""
    
    for sentence in sentences:
        if len(chunk) + len(sentence) < chunk_size:
            chunk += sentence + ". "
        else:
            chunks.append(chunk.strip())
            chunk = sentence + ". "
    
    if chunk:
        chunks.append(chunk.strip())

    return chunks
