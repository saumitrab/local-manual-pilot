import chromadb
from sentence_transformers import SentenceTransformer

# Initialize embedding model and vector database
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
chroma_client = chromadb.PersistentClient(path="./vector_store")
collection = chroma_client.get_or_create_collection(name="manuals")

def store_embeddings(documents):
    """Generate and store embeddings for document chunks."""
    for doc_name, text in documents.items():
        embedding = embedding_model.encode(text).tolist()
        collection.add(ids=[doc_name], embeddings=[embedding], metadatas=[{"source": doc_name}])

def retrieve_answer(query, documents):
    """Retrieve the most relevant document chunk based on the query."""
    query_embedding = embedding_model.encode(query).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=3)
    
    if results["documents"]:
        best_match = results["documents"][0]
        return best_match, results["metadatas"], results["distances"]
    else:
        return "Information not found.", [], []
