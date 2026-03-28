"""Мета-класс для настройки модели и полей формы."""

from django.apps import AppConfig


class CardConfig(AppConfig):
    """Мета-класс для настройки модели и полей формы."""

    name = "card"

    # Поле по умолчанию для автоматически создаваемых первичных ключей
    default_auto_field = "django.db.models.BigAutoField"
