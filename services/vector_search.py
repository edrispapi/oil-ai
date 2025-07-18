import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# بارگیری مدل بردارساز (جمله به وکتور)
model = SentenceTransformer('all-MiniLM-L6-v2')

# فرض: داده نمونه برای ایندکس اولیه
documents = [
    "دستورالعمل بهره‌برداری از چاه گاز فاز ۲ پارس جنوبی",
    "گزارش عملکرد کمپرسور ایستگاه غربی",
    "آموزش تعمیرات پمپ‌های نفتی",
]

# بردارسازی اسناد
doc_vectors = np.array(model.encode(documents)).astype('float32')

# ساخت ایندکس faiss
index = faiss.IndexFlatL2(doc_vectors.shape[1])
index.add(doc_vectors)

def search_documents(query, top_k=3):
    """جستجوی اسناد نزدیک به پرسش بر اساس شباهت معنایی"""
    q_vec = model.encode([query]).astype('float32')
    D, I = index.search(q_vec, top_k)
    results = [documents[i] for i in I[0]]
    return results
