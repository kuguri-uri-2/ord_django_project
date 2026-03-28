"""Представления (views) для приложения card.

Содержит функции-обработчики для отображения списка карточек,
деталей карточки, создания, редактирования и удаления карточек.
"""

from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from .forms import NewCardForm, EditCardForm
from .models import type, Card


def cards(request):
    """
    Отображает список всех карточек с возможностью фильтрации.

    Поддерживает фильтрацию по:
    - Категории (type_id)
    - Поисковому запросу (query) по полям name и example
    """
    search_query = request.GET.get("query", "")
    selected_type = request.GET.get("type", 0)

    category_list = type.objects.all()

    card_queryset = Card.objects.all()

    if selected_type:
        card_queryset = card_queryset.filter(type_id=selected_type)

    if search_query:
        search_filter = Q(name__icontains=search_query) | Q(
            example__icontains=search_query
        )
        card_queryset = card_queryset.filter(search_filter)

    context = {
        "cards": card_queryset,
        "query": search_query,
        "categories": category_list,
        "type_id": int(selected_type),
    }

    return render(request, "card/cards.html", context)


def detail(request, pk):
    """
    Отображает детальную информацию о конкретной карточке.

    Args:
        request: HTTP-запрос
        pk: первичный ключ карточки

    Returns:
        HTTP-ответ с отрендеренным шаблоном detail.html
    """
    card_obj = get_object_or_404(Card, pk=pk)

    related_cards = (
        Card.objects.filter(type=card_obj.type)
        .exclude(pk=card_obj.pk)[:3]
    )

    context = {
        "card": card_obj,
        "related_cards": related_cards,
    }

    return render(request, "card/detail.html", context)


@login_required
def delete(request, pk):
    """
    Удаляет карточку.

    Доступно только автору карточки.
    После удаления перенаправляет на главную страницу таблицы.

    Args:
        request: HTTP-запрос
        pk: первичный ключ удаляемой карточки

    Returns:
        Перенаправление на главную страницу приложения table
    """
    card_to_delete = get_object_or_404(
        Card,
        pk=pk,
        created_by=request.user,
    )

    card_to_delete.delete()

    return redirect("table:index")


@login_required
def new(request):
    """
    Создает новую карточку.

    GET: Отображает пустую форму для создания карточки
    POST: Сохраняет новую карточку и перенаправляет на страницу с деталями

    Args:
        request: HTTP-запрос (GET или POST)

    Returns:
        GET: Форма для создания карточки
        POST (успех): Перенаправление на страницу созданной карточки
        POST (ошибка): Форма с ошибками валидации
    """
    form = None

    if request.method == "POST":
        form = NewCardForm(request.POST, request.FILES)

        if form.is_valid():
            new_card = form.save(commit=False)
            new_card.created_by = request.user
            new_card.save()

            return redirect("card:detail", pk=new_card.pk)
    else:
        form = NewCardForm()

    context = {
        "form": form,
        "title": "new word card",
    }

    return render(request, "card/form.html", context)


@login_required
def edit(request, pk):
    """
    Редактирует существующую карточку.

    Доступно только автору карточки.

    GET: Отображает форму с текущими данными карточки
    POST: Сохраняет изменения и перенаправляет на страницу с деталями

    Args:
        request: HTTP-запрос (GET или POST)
        pk: первичный ключ редактируемой карточки

    Returns:
        GET: Форма с данными карточки
        POST (успех): Перенаправление на страницу карточки
        POST (ошибка): Форма с ошибками валидации
    """
    card_instance = get_object_or_404(
        Card,
        pk=pk,
        created_by=request.user,
    )

    if request.method == "POST":
        form = EditCardForm(
            request.POST,
            request.FILES,
            instance=card_instance,
        )

        if form.is_valid():
            updated_card = form.save()
            return redirect("card:detail", pk=updated_card.pk)
    else:
        form = EditCardForm(instance=card_instance)

    context = {
        "form": form,
        "title": "edit word card",
    }

    return render(request, "card/form.html", context)