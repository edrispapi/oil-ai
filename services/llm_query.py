from services.vector_search import VectorSearchEngine
from services.llm_api import generate_answer

def llm_query(question):
    vector_engine = VectorSearchEngine()
    docs = vector_engine.search(question, top_k=5)
    answer = generate_answer(question, docs)
    return answer
