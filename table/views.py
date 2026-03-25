"""Представления (views) для приложения table."""
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from card.models import Card

def get_user_cards(user):
    """Возвращает QuerySet карточек, принадлежащих пользователю"""
    return Card.objects.filter(created_by=user)


@login_required
def index(request):
    cards_queryset = get_user_cards(request.user)

    return render(
        request=request,
        template_name='table/index.html',
        context={'cards': cards_queryset}
    )
