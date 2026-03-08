"""
Utility functions for the AI Credit Decision System
"""
import os

def ensure_directory_exists(directory_path):
    """Create directory if it doesn't exist"""
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"✓ Created directory: {directory_path}")

def save_text_to_file(filename, text, output_dir="data/extracted_text"):
    """Save extracted text to a file"""
    ensure_directory_exists(output_dir)
    output_path = os.path.join(output_dir, f"{filename}.txt")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)
    
    print(f"✓ Saved extracted text: {output_path}")
    return output_path

def count_words(text):
    """Calculate word count from text"""
    if not text:
        return 0
    return len(text.split())
