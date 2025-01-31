import requests
import json

# Sends the query and retrieved context to LM Studio.
# Retrieves a response from the LLM.
# Handles API request errors gracefully.


# LM Studio API Configuration
LM_STUDIO_API_URL = "http://localhost:5001/generate"  # Ensure LM Studio is running

def generate_response(prompt):
    """Send a query to LM Studio API and return the generated response."""
    payload = {
        "model": "deepseek-r1-distill-qwen-7b",
        "prompt": prompt,
        "temperature": 0.7,
        "max_tokens": 500
    }
    
    try:
        response = requests.post(LM_STUDIO_API_URL, json=payload)
        response_data = response.json()
        return response_data.get("text", "Error: No response from LLM.")
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}"

def get_answer(query, context):
    """Format query with context and get a response from the LLM."""
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return generate_response(prompt)
