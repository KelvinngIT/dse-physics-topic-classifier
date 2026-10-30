import fitz  # PyMuPDF
import re
from typing import List

def extract_text_from_pdf(uploaded_file) -> str:
    """Extract text from uploaded PDF"""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text() + "\n\n"
    doc.close()
    return text

def split_into_questions(text: str) -> List[str]:
    """
    Split full paper text into individual questions.
    Works reasonably well for most DSE papers.
    """
    # Normalize text
    text = re.sub(r'\r\n', '\n', text)
    
    # Split by common question patterns
    pattern = r'(?i)(?:^|\n)\s*(?:Q\.?|Question)?\s*(\d+)[\.\)]\s+'
    parts = re.split(pattern, text)
    
    questions = []
    # parts[0] is text before first question, then number, then content, number, content...
    i = 1
    while i < len(parts) - 1:
        q_num = parts[i]
        q_content = parts[i + 1].strip()
        if len(q_content) > 40:  # filter noise
            questions.append(f"Q{q_num}. {q_content}")
        i += 2
    
    # Fallback: if splitting failed badly, return whole text as one block
    if len(questions) < 3:
        questions = [text]
    
    return questions
