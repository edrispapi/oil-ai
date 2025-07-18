from services.vector_search import search_documents
from services.llm_api import generate_answer
from utils.logger import log_operation

def answer_with_rag(question, user_id):
    retrieved_docs = search_documents(question, top_k=5)
    answer = generate_answer(question, retrieved_docs)
    log_operation("rag_query", {
        "user_id": user_id,
        "question": question,
        "docs": retrieved_docs,
        "answer": answer,
    })
    return answer
