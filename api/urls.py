from django.urls import path
from .views import LLMQueryAPIView

urlpatterns = [
    path('ask-llm/', LLMQueryAPIView.as_view(), name='ask-llm'),
]
