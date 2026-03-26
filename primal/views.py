# views.py — приложение primal
# Основные публичные страницы проекта

from django.shortcuts import render, redirect

from card.models import Card, type
from .forms import Signup


def index(request):
    """
    Представление главной страницы.
    
    Возвращает:
        HttpResponse: отрендеренный шаблон primal/index.html
        с последними карточками и всеми категориями
    """
    all_cards = Card.objects.all()
    all_types = type.objects.all()
    
    template_context = {
        'cards': all_cards,
        'categories': all_types,
    }
    
    return render(request, 'primal/index.html', template_context)


def contact(request):
    """
    Статическая страница с контактами.
    Не принимает параметров и не использует контекст.
    """
    return render(request, 'primal/contact.html', {})


def signup(request):
    """
    Регистрация пользователя.
    
    Поддерживает как GET (показ формы), так и POST (обработка).
    При успехе — редирект на страницу логина.
    """
    template = 'primal/signup.html'
    context = {}
    if request.method == 'POST':
        registration_form = Signup(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return redirect('/login/')
        context['form'] = registration_form
    else:
        context['form'] = Signup()
    return render(request, template, context)
