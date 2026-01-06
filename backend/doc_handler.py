from docx import Document

def extract_text_from_docx(file):
    document = Document(file)
    text = ""

    for para in document.paragraphs:
        text += para.text + "\n"

    return text

