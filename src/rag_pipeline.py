import chromadb
from .embedder import get_embedding_function

# --- CONFIGURATION ---
CHROMA_DB_PATH = "db"
COLLECTION_NAME = "medical_docs"

# Initialize ChromaDB client and collection
client = chromadb.PersistentClient(path=CHROMA_DB_PATH)
embedding_function = get_embedding_function()
collection = client.get_collection(
    name=COLLECTION_NAME, 
    embedding_function=embedding_function # Pass the function directly
)

def retrieve_relevant_chunks(query: str, n_results: int = 5):
    """
    Retrieves the most relevant chunks from the vector store based on the user's query.

    Args:
        query: The user's question.
        n_results: The number of relevant chunks to retrieve.

    Returns:
        A list of document chunks.
    """
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    return results['documents'][0]

def build_prompt(query: str, context_chunks: list) -> str:
    """
    Builds a detailed prompt for the LLM, including the retrieved context.

    Args:
        query: The user's original question.
        context_chunks: A list of relevant text chunks from the database.

    Returns:
        A formatted prompt string.
    """
    context = "\n\n---\n\n".join(context_chunks)
    
    prompt = f"""
You are a helpful medical assistant. Your task is to answer the user's question based ONLY on the provided context.
If the information to answer the question is not in the context, you must state that you cannot find the information in the provided documents.
Do not make up information or use any external knowledge.

Context:
{context}

Question: {query}

Answer:
"""
    return prompt

# This main block is for testing this script independently.
def main():
    """
    Main function to test the RAG pipeline.
    """
    # Example query
    # Replace this with a question relevant to your documents
    user_query = "What are the common treatments for hypertension?" 
    
    print(f"User Query: {user_query}")
    
    # 1. Retrieve relevant chunks
    print("Retrieving relevant context...")
    relevant_chunks = retrieve_relevant_chunks(user_query)
    
    # 2. Build the prompt
    print("Building prompt...")
    prompt = build_prompt(user_query, relevant_chunks)
    
    # 3. Display results
    print("\n--- Retrieved Context Chunks ---")
    for i, chunk in enumerate(relevant_chunks):
        print(f"Chunk {i+1}:\n{chunk}\n")
        
    print("\n--- Generated Prompt for LLM ---")
    print(prompt)

if __name__ == '__main__':
    main()