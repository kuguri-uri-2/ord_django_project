"""Настройки административной панели для приложения card."""

from django.contrib import admin

from .models import Card, type


@admin.register(type)
class TypeAdmin(admin.ModelAdmin):
    """Администрирование модели type."""


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    """Администрирование модели Card."""
