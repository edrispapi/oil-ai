# api/views.py
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import SensorQuerySerializer
from services.rag_pipeline import answer_with_rag

class SensorQueryAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = SensorQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        question = serializer.validated_data["question"]
        answer = answer_with_rag(question, user_id=request.user.id)
        return Response({"answer": answer})
