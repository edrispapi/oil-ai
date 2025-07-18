import json
import faiss
import numpy as np
from kafka import KafkaConsumer
from sentence_transformers import SentenceTransformer
from django.db import transaction
from models.documents import Document
from services.vector_search import update_faiss_index

MODEL = SentenceTransformer('all-MiniLM-L6-v2')

# Consumer راه‌اندازی
consumer = KafkaConsumer(
    'org-data-logs',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

@transaction.atomic
def process_doc(log_record):
    # داده سازمانی: مثلاً لاگ بهره‌برداری سازه نفتی
    title = log_record['title']
    text = log_record['description']
    embedding = MODEL.encode([text])[0].astype('float32').tobytes()
    Document.objects.create(title=title, text=text, embedding=embedding)
    # ایندکس FAISS را به‌روزرسانی کن
    update_faiss_index()

for msg in consumer:
    try:
        process_doc(msg.value)
    except Exception as err:
        # اینجا log_exception را فراخوانی می‌کنیم
        from utils.logger import log_exception
        log_exception('etl_pipeline', str(err))
