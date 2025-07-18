from models.logs import APILog
from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def log_operation(event, data, status_code=200):
    try:
        APILog.objects.create(
            event=event,
            user_id=data.get("user_id"),
            request_data=data,
            response_data={},
            status_code=status_code,
        )
        producer.send('system-logs', {'event': event, 'data': data})
    except Exception as e:
        print("Logging error:", e)
