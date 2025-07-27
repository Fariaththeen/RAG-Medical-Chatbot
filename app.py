import streamlit as st
import chromadb
import os
from chromadb.utils import embedding_functions
from gpt4all import GPT4All
from src.ingestion import ingest_document

# --- CONFIGURATION ---
DATA_DIR = "data"
CHROMA_DB_PATH = "db"
COLLECTION_NAME = "medical_docs"
EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
LLM_MODEL_NAME = "mistral-7b-instruct-v0.1.Q4_0.gguf"

# --- CACHING ---
@st.cache_resource
def load_resources():
    """Loads all necessary models and database clients."""
    print("Loading resources...")
    embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL_NAME)
    client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME, embedding_function=embedding_function)
    llm = GPT4All(LLM_MODEL_NAME)
    print("Resources loaded successfully.")
    return collection, llm

# --- BACKEND LOGIC ---
def retrieve_context(collection, query, n_results=5):
    """Retrieves relevant context from the vector store."""
    results = collection.query(query_texts=[query], n_results=n_results)
    return results['documents'][0]

def generate_response(llm, query, context_chunks):
    """Generates a response using the LLM with the provided context."""
    context = "\n\n---\n\n".join(context_chunks)
    prompt = f"""
You are a medical assistant. Answer the user's question based ONLY on the provided context.
If the context does not contain the answer, state that you cannot find the information in the provided documents.
Context:
{context}
Question: {query}
Answer:
"""
    response = llm.generate(prompt=prompt, max_tokens=1024)
    return response

# --- STREAMLIT UI ---
st.set_page_config(page_title="Medical RAG Assistant", layout="wide")
st.title("🩺 Medical RAG Assistant")

# Load resources
try:
    collection, llm = load_resources()
    st.success("Models and database loaded successfully!")
except Exception as e:
    st.error(f"Failed to load resources. Error: {e}")
    st.stop()

# --- Sidebar for Document Upload ---
with st.sidebar:
    st.header("Upload New Reports")
    uploaded_files = st.file_uploader(
        "Upload PDF files here. They will be processed and added to the knowledge base.",
        type="pdf",
        accept_multiple_files=True
    )
    if st.button("Process Uploaded Files"):
        if uploaded_files:
            with st.spinner("Processing uploaded files... This may take a moment."):
                # Ensure the data directory exists
                if not os.path.exists(DATA_DIR):
                    os.makedirs(DATA_DIR)
                
                for uploaded_file in uploaded_files:
                    file_path = os.path.join(DATA_DIR, uploaded_file.name)
                    # Save the file to disk
                    with open(file_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    
                    # Ingest the new document into ChromaDB
                    ingest_document(file_path, collection)
            
            st.success(f"Successfully processed and added {len(uploaded_files)} file(s) to the knowledge base!")
        else:
            st.warning("Please upload at least one PDF file before processing.")

# --- Main Chat Interface ---
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask a question about your medical documents..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        with st.spinner("Thinking... 🧠"):
            retrieved_chunks = retrieve_context(collection, prompt)
            full_response = generate_response(llm, prompt, retrieved_chunks)
            message_placeholder.markdown(full_response)
        
        with st.expander("Show Retrieved Context"):
            st.json(retrieved_chunks)
            
    st.session_state.messages.append({"role": "assistant", "content": full_response})