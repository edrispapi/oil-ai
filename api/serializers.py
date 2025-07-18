from rest_framework import serializers

class LLMQuerySerializer(serializers.Serializer):
    question = serializers.CharField(required=True, max_length=512)
