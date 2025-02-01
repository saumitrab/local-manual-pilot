# AI Assistant for Appliance Manuals

This project is an AI-powered chat assistant that helps users interact with appliance user manuals by uploading PDFs. It uses **Retrieval-Augmented Generation (RAG)** with **LM Studio's local LLM** for answering queries.

## 🚀 Features
- 📂 Upload and process appliance manuals (PDFs).
- 🔎 Retrieve relevant information using **ChromaDB**.
- 🤖 Generate answers with **LM Studio** (deepseek-r1-distill-qwen-7b).
- 📊 Logs queries, responses, and system performance.

## 📁 Project Structure
```
/ai_assistant/
|-- main.py               # Streamlit UI
|-- pdf_processing.py      # Extracts and stores PDF content
|-- retrieval.py          # Retrieves relevant manual sections
|-- llm_integration.py    # Queries LM Studio for answers
|-- logger.py             # Logs queries & responses
|-- requirements.txt      # Dependencies
|-- assistant_logs.log    # Query log file
```

## 🛠️ Setup & Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/local-manual-pilot/ai-assistant.git
   cd ai-assistant
   ```

2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Ensure **LM Studio** is running with the correct model (`deepseek-r1-distill-qwen-7b`).

4. Run the app:
   ```sh
   streamlit run main.py
   ```

## 🔮 Future Improvements
- ✅ FastAPI backend for better scalability.
- 🌐 Cloud-based vector storage.
- 💡 Rephrased query suggestions.



