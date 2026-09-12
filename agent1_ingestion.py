import os
from pypdf import PdfReader

def extract_text_from_pdf(pdf_path: str, chunk_size: int = 2000) -> list[str]:
    reader = PdfReader(pdf_path)
    full_text = ""
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            full_text += f"\n--- Page {page_num + 1} ---\n" + text
    chunks = [full_text[i:i + chunk_size] for i in range(0, len(full_text), chunk_size)]
    return chunks

if __name__ == "__main__":
    pdf_file = "bda_rmp_2031.pdf"
    if os.path.exists(pdf_file):
        chunks = extract_text_from_pdf(pdf_file)
        print(f"Successfully split PDF into {len(chunks)} chunks.")
    else:
        print("File not found.")