from models.logs import APILog
from kafka import KafkaProducer
import os, json, traceback

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

def log_operation(event, data):
    try:
        APILog.objects.create(
            user_id=data.get("user_id"),
            endpoint=event,
            request_data=data,
            response_data={},
            status_code=200,
        )
        producer.send('system-logs', {'event': event, 'data': data})
    except Exception as e:
        print("Logging error:", str(e))

def log_exception(component, err_message):
    trace = traceback.format_exc()
    producer.send('system-logs', {'event': 'exception', 'component': component, 'trace': trace, 'error': err_message})
    # In production, optionally push to alerting systems, Sentry etc.
