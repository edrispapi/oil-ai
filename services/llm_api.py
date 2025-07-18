# services/llm_api.py
import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_answer(question, context_docs):
    prompt = (
        "بر اساس اطلاعات سنسوری و لاگ‌های صنعتی زیر، به این سؤال فنی پاسخ بده:\n"
        + "\n".join(context_docs)
        + f"\nپرسش: {question}\nپاسخ:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=700,
        temperature=0.2,
    )
    return response.choices[0].message["content"].strip()
