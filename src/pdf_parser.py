import fitz  # PyMuPDF
import os

def parse_pdf(file_path: str) -> str:
    """
    Extracts clean text from a PDF file.

    Args:
        file_path: The path to the PDF file.

    Returns:
        A string containing the extracted text.
    """
    try:
        document = fitz.open(file_path)
        text = ""
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:
        print(f"Error parsing {os.path.basename(file_path)}: {e}")
        return ""

def main():
    """
    Main function to parse all PDFs in the data directory.
    """
    data_dir = "data"
    
    if not os.path.exists(data_dir):
        print(f"Error: The '{data_dir}' directory does not exist. Please create it and add your PDF files.")
        return

    pdf_files = [f for f in os.listdir(data_dir) if f.lower().endswith(".pdf")]

    if not pdf_files:
        print(f"No PDF files found in the '{data_dir}' directory.")
        return

    print(f"Found {len(pdf_files)} PDF(s) to parse...")

    for pdf_file in pdf_files:
        file_path = os.path.join(data_dir, pdf_file)
        print(f"\n--- Parsing: {pdf_file} ---")
        
        extracted_text = parse_pdf(file_path)
        
        if extracted_text:
            # Print a snippet of the extracted text
            print(f"Successfully extracted {len(extracted_text)} characters.")
            print("Snippet:")
            print(extracted_text[:500] + "...")
        else:
            print(f"Could not extract text from {pdf_file}.")

if __name__ == "__main__":
    main()