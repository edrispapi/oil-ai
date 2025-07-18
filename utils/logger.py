from models.logs import APILog

def log_request(user, endpoint, request_data, response_data, status_code):
    try:
        APILog.objects.create(
            user=user,
            endpoint=endpoint,
            request_data=request_data,
            response_data=response_data,
            status_code=status_code,
        )
    except Exception as e:
        # جلوگیری از ایجاد اشکال در اجرای اصلی هنگام بروز خطا در لاگ‌گیری
        pass
