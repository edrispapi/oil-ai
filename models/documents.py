from django.db import models

class Document(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    embedding = models.BinaryField(null=True, blank=True)  # ذخیره بردار معنایی (برای جستجوی برداری)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
