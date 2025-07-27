import os
import chromadb
from chromadb.utils import embedding_functions
from ingestion import ingest_document

# --- 1. SETUP CHROMA DB CLIENT ---
client = chromadb.PersistentClient(path="db")

# --- 2. SETUP EMBEDDING FUNCTION ---
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# --- 3. CREATE/GET COLLECTION ---
collection = client.get_or_create_collection(
    name="medical_docs",
    embedding_function=sentence_transformer_ef,
    metadata={"hnsw:space": "cosine"}
)

def ingest_all_documents():
    """
    Finds all PDFs in the 'data' directory and ingests them into ChromaDB.
    """
    data_dir = "data"
    
    if not os.path.isdir(data_dir):
        print(f"The directory '{data_dir}' does not exist. Please create it and add your PDFs.")
        return

    pdf_files = [f for f in os.listdir(data_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print("No PDF files found in the 'data' directory. Nothing to ingest.")
        return

    print(f"Found {len(pdf_files)} PDF(s) to ingest...")

    for pdf_file in pdf_files:
        file_path = os.path.join(data_dir, pdf_file)
        ingest_document(file_path, collection)

    print("\n--- Ingestion Complete ---")
    print(f"Total documents in collection: {collection.count()}")


if __name__ == "__main__":
    ingest_all_documents()