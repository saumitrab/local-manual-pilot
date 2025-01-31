import chromadb
from sentence_transformers import SentenceTransformer

# This script takes a user query, converts it into an embedding, retrieves relevant
# text chunks from ChromaDB, and returns the response along with citations and a confidence score.

# Initialize embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# Initialize ChromaDB
vector_db = chromadb.PersistentClient(path="./vector_store")
collection = vector_db.get_or_create_collection("manuals")

def retrieve_answer(query, top_k=3):
    """Retrieve the most relevant document chunks for a given query."""
    query_embedding = embedding_model.encode([query])[0].tolist()
    
    # Perform similarity search
    results = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    
    if results['documents']:
        retrieved_texts = results['documents'][0]
        scores = results['distances'][0]
        
        # Format citations and confidence score
        citations = [f"Source {i+1}: {retrieved_texts[i]}" for i in range(len(retrieved_texts))]
        confidence = sum(scores) / len(scores) if scores else 0.0
        
        return " ".join(retrieved_texts), citations, confidence
    else:
        return "No relevant information found.", [], 0.0
