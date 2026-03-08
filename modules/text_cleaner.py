"""
Text cleaning module for financial document processing
"""
import re

def clean_text(text):
    """
    Clean and normalize extracted text from PDFs
    
    Args:
        text (str): Raw extracted text
        
    Returns:
        str: Cleaned and normalized text
    """
    if not text:
        return ""
    
    # Remove extra spaces
    text = re.sub(r' +', ' ', text)
    
    # Remove repeated line breaks (more than 2 consecutive)
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Remove leading/trailing whitespace from each line
    lines = [line.strip() for line in text.split('\n')]
    text = '\n'.join(lines)
    
    # Remove any remaining extra whitespace
    text = text.strip()
    
    print(f"✓ Text cleaned: {len(text)} characters")
    return text
