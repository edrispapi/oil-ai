from django.db import models

class APILog(models.Model):
    user_id = models.IntegerField()
    endpoint = models.CharField(max_length=120)
    request_data = models.JSONField()
    response_data = models.JSONField()
    status_code = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
