# api/serializers.py
from rest_framework import serializers

class SensorQuerySerializer(serializers.Serializer):
    question = serializers.CharField(required=True, max_length=512)
