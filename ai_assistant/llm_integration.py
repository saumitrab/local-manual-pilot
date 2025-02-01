from openai import OpenAI

# LM Studio API Configuration
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")  # Adjust port if needed

def generate_response(prompt):
    """Send a query to LM Studio API and return the generated response."""
    try:
        response = client.chat.completions.create(
            model="deepseek-r1-distill-qwen-7b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

def get_answer(query, context):
    """Format query with context and get a response from the LLM."""
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return generate_response(prompt)
