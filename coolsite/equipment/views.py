from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


from .models import *

menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Добавить продукт", 'url_name': "add_product"},
        {'title': "обратная связь", 'url_name': "contact"},
        {'title': "Войти", 'url_name': "login"},

        ]

def index(request):
    products = Equipment.objects.all()
    cats = Category.objects.all()

    context={
        'products': products,
        'cats': cats,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
    }
    return render(request, 'equipment/index.html', context=context)

def about(request):
    return render(request, 'equipment/about.html', {'menu': menu, 'title': 'about'})

def addpage(request):
    return HttpResponse("addpage")

def contact(request):
    return HttpResponse("contact")

def login(request):
    return HttpResponse("login")


def show_prod(request, prod_id):
    return HttpResponse(f"product with id = {prod_id}")


def show_category(request, cat_id):
    products = Equipment.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(products) == 0:
        raise Http404()

    context={
        'products': products,
        'cats': cats,
        'menu': menu,
        'title': 'Категории',
        'cat_selected': cat_id,
    }
    return render(request, 'equipment/index.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена:(</h1>')