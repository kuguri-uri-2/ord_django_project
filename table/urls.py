"""Представления (views) для приложения table."""
from django.urls import path

from . import views


def table_urlpatterns():
    """Возвращает список маршрутов для приложения table"""
    return [
        path('', views.index, name='index'),
    ]


app_name = 'table'
urlpatterns = table_urlpatterns()
