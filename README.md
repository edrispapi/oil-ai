# Oil & Gas Industrial AI Backend

پروژه‌ای برای پیاده‌سازی تحلیل، مدیریت و پرس‌وجوی هوشمند داده‌های سنسوری و صنعتی در حوزه نفت و گاز با استفاده از مدل‌های زبانی بزرگ (LLM)، جستجوی معنایی، ETL و معماری مدرن و سازمان‌یافته.

---

## 🎯 اهداف

- جمع‌آوری، ETL و تحلیل داده‌های سنسور و لاگ صنعتی (بلادرنگ و آفلاین)
- جستجوی معنایی پیشرفته با FAISS و کش نتایج با Redis
- پاسخ‌گویی حرفه‌ای به پرس‌وجوهای مهندسی و اپراتوری با LLM (مانند OpenAI)
- ادغام با زیرساخت‌های Kafka، SCADA، ERP، داشبورد و ابزارهای پردازش داده

---

## 🏗️ معماری و ابزارها

- **بک‌اند**: Django + Django REST Framework
- **ETL و پیام‌رسانی**: KafkaConsumer, Python
- **جستجوی برداری**: SentenceTransformers, FAISS, Redis
- **ادغام LLM**: OpenAI API / Hugging Face
- **لاگینگ**: Kafka, PostgreSQL, API_LOG سفارشی
- **کانتینرسازی**: Docker, docker-compose
- **تست**: pytest, APITestCase
- **مستندسازی**: Swagger/OpenAPI (drf-yasg)

---


