from langchain.text_splitter import RecursiveCharacterTextSplitter
# This line is only needed if you run this file directly for testing.
# We'll fix it with a relative import to work correctly within the project.
from .pdf_parser import parse_pdf

def chunk_text(raw_text: str, chunk_size: int = 1000, chunk_overlap: int = 100):
    """
    Splits the raw text into smaller chunks.

    Args:
        raw_text: The input text to be chunked.
        chunk_size: The maximum size of each chunk (in characters).
        chunk_overlap: The number of characters to overlap between chunks.

    Returns:
        A list of text chunks.
    """
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks

# This main block is for testing this script independently.
def main():
    """
    Main function to test the chunking process.
    """
    # Note: Replace with a valid path to a PDF in your data folder for testing.
    pdf_path = "data/sample-medical-report.pdf" 
    
    # 1. Parse the PDF
    print(f"Parsing PDF: {pdf_path}")
    parsed_text = parse_pdf(pdf_path)
    
    if parsed_text:
        # 2. Chunk the text
        print("Chunking text...")
        text_chunks = chunk_text(parsed_text)
        
        # 3. Display results
        print(f"Successfully created {len(text_chunks)} chunks.")
        # print("--- First Chunk ---")
        # print(text_chunks[0])
        # print("\n--- Second Chunk ---")
        # print(text_chunks[1])
    else:
        print("Failed to parse PDF.")

if __name__ == '__main__':
    main()
