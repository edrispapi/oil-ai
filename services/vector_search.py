import faiss, redis, json
import numpy as np
from sentence_transformers import SentenceTransformer
from models.documents import Document

EMBEDDING_DIM = 384
embedder = SentenceTransformer('all-MiniLM-L6-v2')
redis_client = redis.Redis(host='redis', port=6379, db=0)
FAISS_INDEX_FILE = 'faiss-index.idx'
_index = None

def load_faiss_index():
    global _index
    if _index is None:
        try:
            _index = faiss.read_index(FAISS_INDEX_FILE)
        except:
            _index = faiss.IndexFlatL2(EMBEDDING_DIM)
    return _index

def update_faiss_index():
    docs = Document.objects.all()
    vecs = np.array([np.frombuffer(d.embedding, dtype='float32') for d in docs if d.embedding])
    index = faiss.IndexFlatL2(EMBEDDING_DIM)
    if len(vecs):
        index.add(vecs)
        faiss.write_index(index, FAISS_INDEX_FILE)

def search_documents(query, top_k=5):
    cache_key = f"vec_search:{query}"
    if redis_client.exists(cache_key):
        return json.loads(redis_client.get(cache_key))
    index = load_faiss_index()
    q_vec = embedder.encode([query]).astype('float32')
    D, I = index.search(q_vec, top_k)
    docs = Document.objects.all()
    result = [docs[i].text for i in I[0]]
    redis_client.set(cache_key, json.dumps(result), ex=300)
    return result
