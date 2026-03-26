"""Формы для аутентификации и регистрации пользователей в приложении primal.

Содержит кастомные формы для входа (LoginForm) и регистрации (Signup)
с стилизованными полями ввода.
"""
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


BASE_WIDGET_KWARGS = {
    'class': 'w-full py-4 px-6 rounded-3xl text-center'
}


FIELD_CONFIG = {
    'username': {
        'widget': forms.TextInput,
        'placeholder': 'name',
    },
    'password': {
        'widget': forms.PasswordInput,
        'placeholder': 'password',
    },
}


class LoginForm(AuthenticationForm):
    """
    Форма для входа пользователя в систему.
    
    Наследуется от стандартной AuthenticationForm и добавляет
    кастомные атрибуты CSS классов и плейсхолдеры для полей.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, config in FIELD_CONFIG.items():
            self.fields[field_name].widget = config['widget'](
                attrs={
                    **BASE_WIDGET_KWARGS,
                    'placeholder': config['placeholder']
                }
            )


SIGNUP_FIELD_CONFIG = {
    'username':     ('text',    'ur name'),
    'email':        ('email',   'mail'),
    'password1':    ('password','came up with password'),
    'password2':    ('password','password again'),
}


class Signup(UserCreationForm):
    """
    Форма для регистрации нового пользователя.
    
    Наследуется от стандартной UserCreationForm и добавляет
    поле email, а также кастомные атрибуты CSS классов и 
    плейсхолдеры для всех полей.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        widget_map = {
            'text': forms.TextInput,
            'email': forms.EmailInput,
            'password': forms.PasswordInput,
        }
        for field_name, (w_type, ph) in SIGNUP_FIELD_CONFIG.items():
            self.fields[field_name].widget = widget_map[w_type](
                attrs={
                    **BASE_WIDGET_KWARGS,
                    'placeholder': ph
                }
            )

    class Meta:
        """Мета-класс для настройки модели и полей формы."""
        model = User
        fields = ('username', 'email', 'password1', 'password2')
