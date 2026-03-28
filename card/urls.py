"""URL-конфигурация для приложения card.

Определяет маршруты URL для просмотра, создания, редактирования и удаления карточек.
"""

from django.urls import path
from . import views

app_name = "card"


routes = [
    path("", views.cards, name="cards"),
    path("new/", views.new, name="new"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/edit/", views.edit, name="edit"),
]

urlpatterns = routes
