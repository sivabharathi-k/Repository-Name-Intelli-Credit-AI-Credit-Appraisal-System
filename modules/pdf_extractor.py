"""
PDF text extraction module for financial documents
"""
import pdfplumber

def extract_text_from_pdf(pdf_file):
    """
    Extract text from a PDF file with robust error handling
    
    Args:
        pdf_file: File object or path to PDF
        
    Returns:
        str: Extracted text from all pages
    """
    extracted_text = ""
    
    try:
        with pdfplumber.open(pdf_file) as pdf:
            total_pages = len(pdf.pages)
            print(f"📄 Processing PDF with {total_pages} pages...")
            
            for page_num, page in enumerate(pdf.pages, 1):
                try:
                    print(f"  → Extracting page {page_num}/{total_pages}")
                    page_text = page.extract_text()
                    
                    # Skip empty pages
                    if page_text and page_text.strip():
                        extracted_text += page_text + "\n\n"
                    else:
                        print(f"  ⚠ Page {page_num} is empty, skipping...")
                        
                except Exception as e:
                    print(f"  ✗ Error extracting page {page_num}: {str(e)}")
                    continue
            
            print(f"✓ Extraction complete: {len(extracted_text)} characters extracted")
            
    except Exception as e:
        print(f"✗ Error opening PDF: {str(e)}")
        raise Exception(f"Failed to process PDF: {str(e)}")
    
    return extracted_text.strip()

def extract_from_multiple_pdfs(pdf_files):
    """
    Extract text from multiple PDF files
    
    Args:
        pdf_files: List of file objects
        
    Returns:
        dict: Dictionary with filename as key and extracted text as value
    """
    results = {}
    
    for pdf_file in pdf_files:
        filename = pdf_file.name
        print(f"\n{'='*60}")
        print(f"Processing: {filename}")
        print(f"{'='*60}")
        
        try:
            text = extract_text_from_pdf(pdf_file)
            results[filename] = {
                'text': text,
                'status': 'success',
                'error': None
            }
        except Exception as e:
            print(f"✗ Failed to process {filename}")
            results[filename] = {
                'text': '',
                'status': 'error',
                'error': str(e)
            }
    
    return results
