# رابط بین جستجوی معنایی و LLM
from .vector_search import search_documents
from .llm_api import generate_answer

def llm_query(question):
    """
    دریافت سوال، بازیابی اسناد مرتبط، ارسال به مدل LLM و بازگشت پاسخ
    """
    # اسناد مشابه معنایی را بیاب
    docs = search_documents(question)
    # تولید پاسخ با LLM
    answer = generate_answer(question, docs)
    return answer
