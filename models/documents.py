from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    source_type = models.CharField(max_length=40)  # مثل: LOG, REPORT, SENSOR, etc.
    meta = models.JSONField(default=dict)
    embedding = models.BinaryField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
