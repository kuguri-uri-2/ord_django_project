"""
Основная URL-конфигурация проекта ord.

Здесь подключаются все приложения и административная панель.
Также включается обслуживание медиа-файлов в режиме разработки.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# Список основных маршрутов проекта
urlpatterns = [
    # Главная часть сайта (primal)
    path('', include('primal.urls')),
    
    # Раздел с карточками
    path('cards/', include('card.urls')),
    
    # Личный кабинет / таблица пользователя
    path('table/', include('table.urls')),
    
    # Админ-панель Django
    path('admin/', admin.site.urls),
]

# Обслуживание медиа-файлов только в режиме DEBUG
if settings.DEBUG:
    urlpatterns += static(
        prefix=settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )