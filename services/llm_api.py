import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_answer(question, context_docs):
    context = '\n'.join([f"- {doc.title}:\n{doc.text}" for doc in context_docs])
    prompt = (
        f"بر اساس اسناد فنی زیر به پرسش داده شده به صورت منسجم، کوتاه و حرفه‌ای پاسخ بده:\n"
        f"{context}\n\nپرسش: {question}\nپاسخ:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=750,
        temperature=0.2,
    )
    return response.choices[0].message["content"].strip()
