# دریافت پرسش کاربر و ارسال به سرویس LLM
from rest_framework.views import APIView
from rest_framework.response import Response
from services.llm_query import llm_query

class LLMQueryAPIView(APIView):
    """
    API برای ارسال پرسش کاربر به موتور LLM و دریافت پاسخ
    """
    def post(self, request):
        question = request.data.get('question', '')
        if not question:
            return Response({'error': 'Question is required'}, status=400)
        answer = llm_query(question)
        return Response({'answer': answer})
