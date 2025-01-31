import streamlit as st
from pdf_processing import process_pdfs
from retrieval import retrieve_answer
import os

# Streamlit UI
st.set_page_config(page_title="AI Assistant for Appliance Manuals")

st.title("AI Assistant for Appliance Manuals")

# Sidebar for PDF Upload
st.sidebar.header("Upload PDF Manuals")
uploaded_files = st.sidebar.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    pdf_texts = process_pdfs(uploaded_files)
    st.sidebar.success("PDFs processed successfully!")

# User Query Input
query = st.text_input("Ask a question about your appliance manual:")

if query:
    response, citations, confidence = retrieve_answer(query)
    st.write("### Answer:")
    st.write(response)

    # Display citations and confidence score
    if citations:
        st.write("#### Citations:")
        for citation in citations:
            st.write(f"- {citation}")
    
    st.write(f"**Confidence Score:** {confidence:.2f}")

st.sidebar.info("Ensure LM Studio is running with the required model.")

if __name__ == "__main__":
    st.sidebar.text("Ready for queries!")
