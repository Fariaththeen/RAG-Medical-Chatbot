from sentence_transformers import SentenceTransformer
from .chunker import chunk_text
from .pdf_parser import parse_pdf

# Define the embedding model
MODEL_NAME = "all-MiniLM-L6-v2"

def get_embedding_function():
    """
    Returns an embedding function using the SentenceTransformer model.
    """
    model = SentenceTransformer(MODEL_NAME)
    
    def embedding_function(texts):
        # The model.encode function can take a list of strings and returns a list of embeddings
        return model.encode(texts, convert_to_numpy=True)
        
    return embedding_function

# This main block is for testing this script independently.
def main():
    """
    Main function to test the embedding process.
    """
    # Note: Replace with a valid path to a PDF in your data folder for testing.
    pdf_path = "data/sample-medical-report.pdf" 
    
    print(f"Parsing PDF: {pdf_path}")
    raw_text = parse_pdf(pdf_path)
    
    if raw_text:
        print("Chunking text...")
        text_chunks = chunk_text(raw_text)
        
        if text_chunks:
            print("Generating embeddings for chunks...")
            embed_fn = get_embedding_function()
            embeddings = embed_fn(text_chunks)
            
            print(f"Successfully generated {len(embeddings)} embeddings.")
            print(f"Shape of the first embedding: {embeddings[0].shape}")
            # print(f"First embedding vector (first 5 values): {embeddings[0][:5]}")
        else:
            print("No chunks were generated.")
    else:
        print("Failed to parse PDF.")

if __name__ == '__main__':
    main()