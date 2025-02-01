import streamlit as st
from pdf_processing import process_pdfs, process_local_manuals
from retrieval import retrieve_answer
import os
from llm_integration import get_answer

# Streamlit UI
st.set_page_config(page_title="AI Assistant for Appliance Manuals")

st.title("AI Assistant for Appliance Manuals")

# Sidebar for PDF Upload
st.sidebar.header("Upload PDF Manuals")
uploaded_files = st.sidebar.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if 'initialized' not in st.session_state:
    process_local_manuals()
    st.session_state.initialized = True

if uploaded_files:
    pdf_texts = process_pdfs(uploaded_files)
    st.sidebar.success("PDFs processed successfully!")

# User Query Input
query = st.text_input("Ask a question about your appliance manual:")

if query:
    # Get initial context and response from retrieval
    response, citations, confidence = retrieve_answer(query)
    
    # Prepare assistant's response using LLM
    system_prompt = "I am an AI assistant specialized in helping with home appliance manuals."
    user_context = f"Question: {query}\nContext: {response}\nConfidence: {confidence}"
    
    if confidence > 0.5 and response:
        # Construct and verify response
        final_response = get_answer(system_prompt, user_context)
        
        # Display response
        st.write("### Answer:")
        st.write(final_response)
        
        # Show citations if available
        if citations:
            st.write("#### Supporting Information:")
            for citation in citations:
                st.write(f"- {citation}")
    else:
        st.write("I apologize, but I don't have enough information to provide a reliable answer to your question.")

st.sidebar.info("Ensure LM Studio is running with the required model.")

if __name__ == "__main__":
    st.sidebar.text("Ready for queries!")
