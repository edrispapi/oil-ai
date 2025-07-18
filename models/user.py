from django.contrib.auth.models import AbstractUser
from django.db import models

class OilGasUser(AbstractUser):
    ROLE_CHOICES = (
        ('engineer', 'مهندس'),
        ('admin', 'مدیر سیستم'),
        ('operator', 'اپراتور'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='engineer')

    def __str__(self):
        return f"{self.username} ({self.role})"
