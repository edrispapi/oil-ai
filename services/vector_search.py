import faiss
import numpy as np
import redis
from sentence_transformers import SentenceTransformer
from models.documents import Document

MODEL = SentenceTransformer('all-MiniLM-L6-v2')
REDIS = redis.Redis(host='redis', port=6379, db=0)

# FAISS index مدیریت
INDEX_FILE = 'faiss_index.index'
EMBEDDING_DIM = 384
_index = None

def load_faiss_index():
    global _index
    if _index is None:
        try:
            _index = faiss.read_index(INDEX_FILE)
        except:
            _index = faiss.IndexFlatL2(EMBEDDING_DIM)
    return _index

def update_faiss_index():
    docs = Document.objects.all()
    vecs = np.array([np.frombuffer(d.embedding, dtype='float32') for d in docs])
    index = faiss.IndexFlatL2(EMBEDDING_DIM)
    if len(vecs): index.add(vecs)
    faiss.write_index(index, INDEX_FILE)

def search_documents(query, top_k=5):
    cache_key = f'vector_search:{query}'
    if REDIS.exists(cache_key):
        return json.loads(REDIS.get(cache_key))
    index = load_faiss_index()
    q_vec = MODEL.encode([query]).astype('float32')
    D, I = index.search(q_vec, top_k)
    docs = Document.objects.all()
    result = [docs[i].text for i in I[0]]
    REDIS.set(cache_key, json.dumps(result), ex=300)
    return result
