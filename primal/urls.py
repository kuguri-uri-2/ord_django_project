"""URL-конфигурация для приложения primal.

Определяет маршруты URL для главной страницы, контактов,
регистрации и входа в систему.
"""
from django.contrib.auth import views as auth_views
from django.urls import path

from .views import index, contact, signup
from .forms import LoginForm

app_name = 'primal'

urlpatterns = [
    path(**{'route': '',        'view': index,   'name': 'index'}),
    path(**{'route': 'contact/', 'view': contact, 'name': 'contact'}),
    path(**{'route': 'signup/',  'view': signup,  'name': 'signup'}),
    path(
        'login/',
        auth_views.LoginView.as_view(
            **{
                'template_name': 'primal/login.html',
                'authentication_form': LoginForm,
            }
        ),
        name='login',
    ),
]