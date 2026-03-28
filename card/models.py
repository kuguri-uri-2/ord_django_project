"""URL-конфигурация для приложения card.

Определяет маршруты URL для просмотра, создания, редактирования и удаления карточек.
"""

from django.contrib.auth.models import User
from django.db import models


class type(models.Model):
    """URL-конфигурация для приложения card.

    Определяет маршруты URL для просмотра, создания, редактирования и удаления карточек.
    """

    name = models.CharField(
        max_length=255,
    )

    class Meta:
        """URL-конфигурация для приложения card.

        Определяет маршруты URL для просмотра, создания, редактирования и удаления карточек.
        """

        ordering = ["name"]
        verbose_name_plural = "темы"

    def __str__(self):
        value = self.name
        return value


class Card(models.Model):
    """URL-конфигурация для приложения card.

    Определяет маршруты URL для просмотра, создания, редактирования и удаления карточек.
    """

    created_by = models.ForeignKey(
        User,
        related_name="cards",
        on_delete=models.CASCADE,
    )

    type = models.ForeignKey(
        type,
        related_name="cards",
        on_delete=models.CASCADE,
    )

    name = models.CharField(
        max_length=255,
    )

    translation = models.TextField(
        blank=True,
        null=True,
    )

    example = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        card_name = self.name
        return card_name
