from .vector_search import search_documents
from .llm_api import generate_answer

def llm_query(question):
    docs = search_documents(question)
    answer = generate_answer(question, docs)
    return answer
