from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *

menu = [{'title': "О сайте", 'url_name': "about"},
        {'title': "Добавить продукт", 'url_name': "add_product"},
        {'title': "обратная связь", 'url_name': "contact"},
        {'title': "Войти", 'url_name': "login"},

        ]


class Home(ListView):
    model = Equipment
    template_name = 'equipment/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Equipment.objects.filter(is_published=True)


def about(request):
    return render(request, 'equipment/about.html', {'menu': menu, 'title': 'about'})


def contact(request):
    return HttpResponse("contact")


def add_page(request):
    return HttpResponse("contact")


def login(request):
    return HttpResponse("login")

class show_prod(DetailView):
    model = Equipment
    template_name = 'equipment/product.html'
    slug_url_kwarg = 'prod_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['product']
        return context


class Category(ListView):
    model = Equipment
    template_name = 'equipment/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория' + str(context['products'][0].cat)
        context['cat_selected'] = context['products'][0].cat_id
        return context

    def get_queryset(self):
        return Equipment.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена:(</h1>')