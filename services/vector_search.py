import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from models.documents import Document

EMBEDDING_DIM = 384
MODEL = SentenceTransformer('all-MiniLM-L6-v2')

class VectorSearchEngine:
    def __init__(self):
        # بازیابی اسناد فعال از دیتابیس و آماده سازی ایندکس
        docs = Document.objects.all()
        texts = [d.text for d in docs]
        embeddings = np.array([MODEL.encode(t) for t in texts]).astype('float32')
        self.texts_map = dict(enumerate(docs))
        self.index = faiss.IndexFlatL2(EMBEDDING_DIM)
        if embeddings.shape[0]:
            self.index.add(embeddings)
    
    def search(self, query, top_k=5):
        q_vec = MODEL.encode([query]).astype('float32')
        D, I = self.index.search(q_vec, top_k)
        return [self.texts_map[i] for i in I[0]]

# این کلاس را می توان در startup هر سرور یا در بازسازی ایندکس فراخوانی کرد.
