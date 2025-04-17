import re
import PyPDF2
from docx import Document

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            return " ".join([page.extract_text() or "" for page in reader.pages])
    elif file_path.endswith(".docx"):
        doc = Document(file_path)
        return " ".join([p.text for p in doc.paragraphs])
    return ""

def extract_contact_info(text, filename):
    email = re.search(r"[\\w.-]+@[\\w.-]+", text)
    return {"email": email.group(0) if email else "unknown@example.com", "name": filename.split('.')[0]}
