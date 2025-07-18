# models/logs.py
from django.db import models

class APILog(models.Model):
    event = models.CharField(max_length=120)
    user_id = models.IntegerField(null=True)
    request_data = models.JSONField()
    response_data = models.JSONField()
    status_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
