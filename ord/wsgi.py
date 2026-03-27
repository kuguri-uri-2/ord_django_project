"""
WSGI entry point для проекта ord.

Этот файл отвечает за запуск WSGI-приложения Django.
Подробнее: https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Устанавливаем переменную окружения с модулем настроек
os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    'ord.settings'
)

# Создаём WSGI-приложение
application = get_wsgi_application()