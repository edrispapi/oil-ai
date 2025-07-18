INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework_simplejwt',
    # سایر اپ‌ها
    'api',
    'models',
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.IsAuthenticated",
    ),
}

OPENAI_API_KEY = 'کلید_امن'
