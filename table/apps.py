"""Конфигурация приложения table для Django проекта."""
from django.apps import AppConfig


class TableConfig(AppConfig):
    """
    Конфигурация класса для приложения table.
    
    Определяет настройки Django-приложения, включая поле автоматического
    инкремента по умолчанию и имя приложения.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'table'
