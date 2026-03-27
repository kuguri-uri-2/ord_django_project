"""
ASGI-конфигурация проекта ord

Экспортирует ASGI-приложение как переменную application.
Подробнее: https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# Устанавливаем модуль настроек по умолчанию
os.environ.setdefault(
    key='DJANGO_SETTINGS_MODULE',
    value='ord.settings'
)

# Инициализация ASGI-приложения
application = get_asgi_application()