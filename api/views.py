from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import LLMQuerySerializer
from services.llm_query import llm_query
from utils.logger import log_request

class LLMQueryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LLMQuerySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        question = serializer.validated_data['question']
        answer = llm_query(question)
        log_request(user, '/api/ask-llm/', request.data, {'answer': answer}, 200)
        return Response({'answer': answer})
