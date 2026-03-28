"""Формы для приложения card.

Содержит формы для создания (NewCardForm) и редактирования (EditCardForm) карточек
с единым стилем оформления полей ввода.
"""

from django import forms

from .models import Card


INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


def styled_widget(widget_class):
    """Возвращает виджет с применённым CSS-классом."""
    return widget_class(attrs={"class": INPUT_CLASSES})


class NewCardForm(forms.ModelForm):
    """
    Форма для создания новой карточки.

    Используется для добавления новых слов/карточек в систему.
    Содержит поля: name (слово), translation (перевод),
    example (пример использования) и type (категория).
    """

    class Meta:
        """Мета-класс для настройки модели и полей формы."""
        model = Card

        fields = (
            "type",
            "name",
            "translation",
            "example",
        )

        widgets = {
            "type": styled_widget(forms.Select),
            "name": styled_widget(forms.TextInput),
            "translation": styled_widget(forms.TextInput),
            "example": styled_widget(forms.Textarea),
        }


class EditCardForm(forms.ModelForm):
    """
    Форма для редактирования существующей карточки.

    Используется для изменения данных существующей карточки.
    В отличие от формы создания, не позволяет изменять категорию (type).
    """

    class Meta:
        """Мета-класс для настройки модели и полей формы."""
        model = Card

        fields = (
            "name",
            "translation",
            "example",
        )

        widgets = {
            "name": styled_widget(forms.TextInput),
            "translation": styled_widget(forms.TextInput),
            "example": styled_widget(forms.Textarea),
        }
