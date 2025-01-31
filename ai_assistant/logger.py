import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="assistant_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_query(user_query, retrieved_docs, response, confidence):
    """Log user queries, retrieved documents, and responses."""
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "user_query": user_query,
        "retrieved_docs": retrieved_docs,
        "response": response,
        "confidence": confidence
    }
    logging.info(log_entry)

def log_error(error_message):
    """Log any errors encountered."""
    logging.error(f"{datetime.now().isoformat()} - ERROR - {error_message}")
