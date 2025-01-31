import json
import os
from datetime import datetime

class Logger:
    def __init__(self, log_filename="interactions.log"):
        self.log_dir = "logs"
        os.makedirs(self.log_dir, exist_ok=True)
        self.log_path = os.path.join(self.log_dir, log_filename)

    def log_interaction(self, query, response, context=None):
        data = {
            "timestamp": datetime.now().isoformat(),
            "query": query,
            "response": response,
            "context": context or []
        }
        with open(self.log_path, "a") as f:
            f.write(json.dumps(data) + "\n")
