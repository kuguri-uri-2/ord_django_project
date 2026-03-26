"""Конфигурация приложения primal для Django проекта."""
from django.apps import AppConfig


class PrimalConfig(AppConfig):
    """
    Конфигурация класса для приложения primal.
    
    Определяет настройки Django-приложения, включая поле автоматического
    инкремента по умолчанию и имя приложения.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'primal'
