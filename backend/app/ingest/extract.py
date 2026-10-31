import pymupdf as fitz # PyMuPDF
from typing import List, Dict, Any

def extract_pdf_text_and_boxes(file_path: str) -> List[Dict[str, Any]]:
    doc = fitz.open(file_path)
    extracted_data = []

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        words = page.get_text("words")

        boxes = []
        for w in words:
            # w = (x0, y0, x1, y1, "word", block_no, line_no, word_no)
            boxes.append({
                "x0": w[0],
                "y0": w[1],
                "x1": w[2],
                "y1": w[3],
                "word": w[4]
            })

        extracted_data.append({
            "page_number": page_num,
            "page_width": page.rect.width,
            "page_height": page.rect.height,
            "text": text,
            "boxes": boxes
        })

    return extracted_data

if __name__ == "__main__":
    print("Extraction script loaded successfully.")
