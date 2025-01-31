import streamlit as st
import os
from pdf_processing import load_pdfs
from retrieval import retrieve_answer
from llm_integration import query_llm
import logger

# Streamlit UI Setup
st.set_page_config(page_title="AI Assistant for Manuals", layout="wide")
st.title("Chat with Your Appliance Manuals")

# Sidebar for PDF directory selection
pdf_folder = st.sidebar.text_input("Enter the path to the folder containing PDFs:")
if pdf_folder and os.path.exists(pdf_folder):
    st.sidebar.success("PDFs loaded successfully!")
    documents = load_pdfs(pdf_folder)
else:
    st.sidebar.warning("Enter a valid folder path.")

# Chat interface
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask a question about your manuals:")
if st.button("Send") and user_input:
    response, citations, confidence = retrieve_answer(user_input, documents)
    final_response = query_llm(response)
    
    # Logging
    logger.log_interaction(user_input, final_response, confidence, citations)
    
    # Display conversation history
    st.session_state.chat_history.append((user_input, final_response))
    for query, reply in st.session_state.chat_history:
        st.text_area("You:", query, height=30, disabled=True)
        st.text_area("Assistant:", reply, height=100, disabled=True)
    
    # Display citations and confidence score
    st.write(f"**Confidence:** {confidence}")
    st.write(f"**Citations:** {', '.join(citations)}")
