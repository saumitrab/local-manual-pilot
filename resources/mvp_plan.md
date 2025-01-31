# AI Assistant MVP Implementation Plan

## Overview

This document outlines the implementation plan for an AI-powered chat assistant that allows users to interact with appliance user manuals by uploading PDFs. The system will use Retrieval-Augmented Generation (RAG) with LM Studio's local LLM for answering user queries. The implementation will be based on Streamlit for the frontend, using a modular structure that can be extended to FastAPI in the future.

## Architecture

1. **Frontend (Streamlit)**
   - Sidebar for selecting a folder containing PDFs.
   - Chat interface similar to ChatGPT.
   - Display retrieved responses, confidence scores, and citations.
2. **Backend (Within Streamlit, Modularized)**
   - PDF ingestion and preprocessing.
   - Embedding generation and storage.
   - Query handling and retrieval.
   - LM Studio API integration for response generation.
   - Logging queries and responses to a local file.

## Implementation Details

### 1. PDF Processing and Embedding Storage

- **Extract text from PDFs**: Use `PyMuPDF` or `pdfplumber`.
- **Semantic Chunking**: Utilize `LangChain` or `Unstructured` to split text into meaningful sections.
- **Generate Embeddings**: Use `sentence-transformers` for text vectorization.
- **Store Embeddings**: Use `ChromaDB`, the most widely used lightweight local vector database.

### 2. Query Handling and Retrieval

- **Convert user query to vector representation**.
- **Retrieve relevant chunks** from ChromaDB based on similarity search.
- **Pass retrieved context to LM Studio LLM** for answer generation.

### 3. LM Studio Integration

- **Direct API calls to LM Studio** using `deepseek-r1-distill-qwen-7b`.
- **Log API calls** and responses to a local file for debugging and tracking.

### 4. Quality Control & Response Validation

- **Cross-check generated response** with retrieved text to ensure accuracy.
- **Display confidence score and citations** alongside responses.

### 5. Logging & Analytics

- **Log user queries, retrieved documents, and generated responses** to a local file.
- **Store system performance metrics** (e.g., response times, retrieval accuracy) for future improvements.

## Setup and Environment Configuration

### 1. Install Dependencies

Create a `requirements.txt` file with the following content:

```
streamlit
PyMuPDF
pdfplumber
sentence-transformers
chromadb
langchain
requests
```

Then, install dependencies using:

```
pip install -r requirements.txt
```

### 2. Local Setup Steps

- Ensure LM Studio is installed and running with `deepseek-r1-distill-qwen-7b` model loaded.
- Set up a directory for storing PDF manuals.
- Run the Streamlit app:

```
streamlit run main.py
```

## Folder Structure

```
/ai_assistant/
|-- main.py  # Streamlit UI
|-- pdf_processing.py  # PDF ingestion, chunking, embedding
|-- retrieval.py  # Query handling, vector search
|-- llm_integration.py  # LM Studio API calls
|-- logger.py  # Logging mechanism
|-- requirements.txt  # Dependencies
```

## Future Scalability

- **Easily migrate backend to FastAPI** if needed.
- **Expand to cloud-based vector databases** if storage needs increase.
- **Introduce rephrased query suggestions** if needed later.

## Next Steps

1. Set up a basic Streamlit interface.
2. Implement PDF ingestion and vector storage.
3. Develop query retrieval and LM Studio integration.
4. Add quality checks and logging.
5. Test with sample manuals and refine accuracy.

---

This plan ensures a robust and modular implementation with an easy path for future scalability while keeping the MVP simple and efficient. Let me know if any refinements are needed!

