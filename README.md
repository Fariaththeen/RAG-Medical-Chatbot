# 🩺 Medical RAG Assistant

This project is a fully functional, local, and private Retrieval-Augmented Generation (RAG) assistant. It uses a local Large Language Model (LLM) to answer questions about medical documents that you provide, ensuring your data remains completely private.

The system is built to be accurate and reliable, answering questions only based on the provided documents and refusing to answer when the information is not found, thus preventing hallucinations.

---

## ✨ Features

-   **Document Parsing:** Extracts text from PDF files.
-   **Text Chunking:** Splits documents into smaller, meaningful chunks for better retrieval.
-   **Vectorization:** Converts text chunks into numerical embeddings using `all-MiniLM-L6-v2`.
-   **Vector Store:** Stores and indexes embeddings in a local, persistent `ChromaDB` database.
-   **Local LLM:** Uses `GPT4All` to run the `Mistral-7B` model locally on your CPU.
-   **RAG Pipeline:** Retrieves relevant context from the database to answer user queries.
-   **Web Interface:** A simple and interactive UI built with `Streamlit`.

---

## 📂 Project Structure

```
.
├── app.py                  # Main Streamlit application file
├── data/                   # Directory to store your PDF documents
│   └── (add your pdfs here)
├── db/                     # Directory for the persistent ChromaDB vector store
├── src/                    # Source code for the backend pipeline
│   ├── pdf_parser.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_store_setup.py
│   ├── rag_pipeline.py
│   └── llm_integration.py
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

---

## 🚀 Getting Started

### 1. Prerequisites

-   Python 3.8 or higher
-   `pip` package manager

### 2. Installation

Clone the repository and install the required dependencies:

```bash
# Clone this project
git clone <repository_url>
cd <repository_directory>

# Install dependencies
pip install -r requirements.txt
```

### 3. Add Your Documents

Place all the PDF files you want the assistant to know about into the `data/` directory.

### 4. Ingest Documents into the Vector Store

Run the ingestion script to parse, chunk, and embed your documents. This only needs to be done once, or whenever you add new documents.

```bash
python src/vector_store_setup.py
```

### 5. Run the Application

Launch the Streamlit web application.

```bash
streamlit run app.py
```

The first time you run this, it will download the `mistral-7b-instruct-v0.1.Q4_0.gguf` model (approx. 4 GB). This is a one-time download.

Your web browser will open with the chat interface, and you can start asking questions!

---

## 🛠️ Technology Stack

-   **Backend:** Python
-   **Web UI:** Streamlit
-   **LLM:** GPT4All (Mistral-7B)
-   **Vector Database:** ChromaDB
-   **Embedding Model:** Sentence-Transformers (`all-MiniLM-L6-v2`)
-   **PDF Parsing:** PyMuPDF
-   **Text Processing:** LangChain
```

This completes our project. You have successfully built a powerful and private AI assistant from the ground up. Well done