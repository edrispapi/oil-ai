# api/urls.py
from django.urls import path
from .views import SensorQueryAPIView

urlpatterns = [
    path('sensor-query/', SensorQueryAPIView.as_view(), name='sensor_query'),
]
