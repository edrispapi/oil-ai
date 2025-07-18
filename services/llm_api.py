import openai

openai.api_key = "کلید_API_خودتان"

def generate_answer(question, context_docs):
    """ارسال پرسش و اسناد به GPT و دریافت پاسخ"""
    prompt = (
        "بر اساس اسناد زیر به پرسش پاسخ بده:\n\n"
        + "\n\n".join(context_docs)
        + "\n\nپرسش: " + question + "\nپاسخ:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=512,
        temperature=0.2,
    )
    return response.choices[0].message["content"].strip()
