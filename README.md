

```
# Oil & Gas Industrial AI Backend

پروژه‌ای جامع برای **تحلیل، مدیریت و پاسخ‌گویی هوشمند به داده‌های صنعتی نفت و گاز** با محوریت مدل‌های زبانی بزرگ (LLM)، پردازش داده‌های سنسور، جستجوی معنایی برداری، ETL، کش، و معماری ماژولار بر پایه Django.

---

## 🎯 هدف پروژه

- جمع‌آوری و تحلیل داده‌های واقعی سنسور و لاگ عملیات (برخط و دسته‌ای)
- جستجوی معنایی پیشرفته بر داده‌های صنعتی (با FAISS و Redis)
- پاسخ‌گویی هوشمند و تخصصی به پرسش‌های اپراتورها و مهندسین میدان، با استفاده از LLM (OpenAI یا مدل بومی)
- قابلیت ادغام با زیرساخت‌های ابری، Kafka، SCADA، ERP و Dashboardهای مانیتورینگ

---

## 🏗️ معماری و فناوری‌ها

- **Backend Framework**: Django + Django REST Framework
- **Vector Search**: FAISS + SentenceTransformers
- **LLM Integration**: OpenAI API (یا مدل‌های Hugging Face)
- **ETL Pipeline**: Python (KafkaConsumer, SentenceTransformer)
- **Cache**: Redis
- **Log/Stream**: Kafka + PostgreSQL
- **Containerization**: Docker, docker-compose  
- **Testing**: pytest, APITestCase  
- **Documentation**: Swagger/OpenAPI (drf-yasg)

---

## 📂 ساختار دایرکتوری

```
oilgas_llm_backend/
│
├── api/                # Endpointهای REST و سریالایزرها
├── services/           # سرویس‌های رگ، برداری، LLM، و ...
├── etl/                # پردازش ETL و kafka consumer
├── models/             # مدل‌های داده‌ای (اسناد، لاگ، کاربر)
├── utils/              # ابزار کمکی، لاگینگ، کش
├── tests/              # تست‌های واحد بخش‌های مختلف
├── requirements.txt    # وابستگی‌ها
├── docker-compose.yml  # استقرار چندسرویسی
├── Dockerfile          
├── settings.py         
└── README.md
```

---

## ⚡ ویژگی‌ها

- پردازش سنسور و لاگ صنعتی برخط از Kafka (قابل توسعه برای SCADA/ERP)
- ETL، بردارسازی متن، ثبت داده ساخت‌یافته، و ایندکس سریع
- جستجوی معنایی با FAISS و کش نتایج با Redis
- سرویس پرسش و پاسخ رگ + LLM برای استنتاج تخصصی (RAG)
- API ایمن، احراز هویت و سطوح دسترسی کاربران
- مستندسازی API با Swagger (در مسیر `/swagger/`)
- تست واحد و یکپارچه، قابلیت استقرار بر روی Docker

---

## 🚀 نحوه اجرا (Locally)

```
# ۱. نصب پیش‌نیازها
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# ۲. کانفیگ متغیرهای محیطی (.env)
cp .env.example .env
# مقداردهی کلیدهای API، تنظیمات DB، Redis، Kafka و OpenAI

# ۳. اجرای Docker (ترجیحاً)
docker-compose up --build

# ۴. (اختیاری) مهاجرت جداول دیتابیس
docker-compose exec web python manage.py migrate

# ۵. راه‌اندازی kafka consumer (etl)
docker-compose exec web python etl/etl_pipeline.py

# ۶. دسترسی به API
# مثال: POST به /api/sensor-query/ با پارامتر {'question': 'علت افت فشار چاه x؟'}
```

---

## 🧪 تست

```
pytest
# یا
python manage.py test
```

---

## 🛡️ راهنمای امنیت و توسعه

- از فایل `.env` برای اطلاعات حساس/کلیدها استفاده کنید.
- برای محیط prod حتماً کلیدها و دسترسی‌ها را محدود کنید.
- داکر را با شبکه غیرعمومی و مدیریت secrets اجرا کنید.
- پوشه tests/ را برای پوشش بالای کد گسترش دهید.
- Swagger در مسیر `/swagger/` مستندسازی کامل REST‌API را نمایش می‌دهد.

---

## 👥 مدیریت کاربران و نقش‌ها

- مبتنی بر مدل کاربر سفارشی جنگو با نقش (مهندس، مدیر، اپراتور)
- دسترسی ماژولار endpointها و پنل مدیریت

---

## 📝 وضعیت توسعه

- [x] ETL و مصرف داده برخط Kafka
- [x] جستجوی برداری و کش نتایج
- [x] ادغام مدل LLM (OpenAI)
- [x] مستندسازی کامل API
- [x] مدیریت لاگ و ردیابی عملیات
- [x] تست واحد و یکپارچه
- [ ] داشبورد مدیریتی (در دست توسعه)
- [ ] پشتیبانی از مدل LLM بومی (به‌زودی)
- [ ] قابلیت بارگذاری اسناد PDF و فایل‌های صنعتی

---

## 💬 مشارکت و توسعه

پذیرای Pull Request و Issue هستیم!
برای گسترش امکانات با معماری مدرن، طبقه‌بندی سرویس‌ها و بهبود مستندسازی کد، پیشنهادها و همکاری ارزشمند است.

---

## 📄 مجوز

MIT License

---

> طراحی‌شده ویژه پروژه‌های داده‌محور، مبتنی بر هوش مصنوعی و LLM در صنایع نفت، گاز و انرژی  
> توسعه: تیم شما — ۲۰۲۵
```

