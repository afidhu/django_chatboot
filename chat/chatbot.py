# chat/chatbot.py
from .utils import get_answer

def ask_question(question: str):
    """Return answer for a given question using FAISS vector search."""
    return get_answer(question)