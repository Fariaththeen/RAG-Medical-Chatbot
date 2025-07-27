import os
from .pdf_parser import parse_pdf
from .chunker import chunk_text

def ingest_document(file_path: str, collection):
    """
    Parses, chunks, and ingests a single document into the ChromaDB collection.

    Args:
        file_path (str): The path to the PDF file.
        collection: The ChromaDB collection object to which the document will be added.
    """
    try:
        pdf_file_name = os.path.basename(file_path)
        
        # 1. Parse PDF
        raw_text = parse_pdf(file_path)
        if not raw_text:
            print(f"Failed to extract text from {pdf_file_name}. Skipping.")
            return

        # 2. Chunk Text
        text_chunks = chunk_text(raw_text)
        if not text_chunks:
            print(f"No chunks created for {pdf_file_name}. Skipping.")
            return
        
        # 3. Prepare data for ChromaDB
        ids = [f"{pdf_file_name}_chunk_{i}" for i in range(len(text_chunks))]
        metadatas = [{"source": pdf_file_name} for _ in range(len(text_chunks))]

        # 4. Ingest into ChromaDB
        # The `add` method handles embedding and storage automatically.
        collection.add(
            documents=text_chunks,
            metadatas=metadatas,
            ids=ids
        )
        print(f"Successfully ingested {len(text_chunks)} chunks from {pdf_file_name}.")

    except Exception as e:
        print(f"An error occurred during ingestion of {file_path}: {e}")
