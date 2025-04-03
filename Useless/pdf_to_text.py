import PyPDF2
import sys

def convert_pdf_to_text(pdf_path, txt_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page_num in range(len(reader.pages)):
            text += reader.pages[page_num].extract_text()
            text += "\n\n--- Page Break ---\n\n"  # Add marker between pages
    
    with open(txt_path, 'w', encoding='utf-8') as output:
        output.write(text)
    
    print(f"Converted '{pdf_path}' to '{txt_path}'")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pdf_to_text.py input.pdf output.txt")
    else:
        convert_pdf_to_text(sys.argv[1], sys.argv[2])