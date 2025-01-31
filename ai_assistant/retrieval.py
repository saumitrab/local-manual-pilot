import chromadb
from sentence_transformers import SentenceTransformer
# ...existing code...

class QueryHandler:
    def __init__(self, db_path="./vector_store"):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.db_client = chromadb.PersistentClient(path=db_path)
        self.collection = self.db_client.get_or_create_collection(name="manuals")

    def retrieve(self, query, n_results=3):
        # ...existing code...
        query_embedding = self.model.encode(query).tolist()
        results = self.collection.query(query_embeddings=[query_embedding], n_results=n_results)
        return results
