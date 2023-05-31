from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView

from .models import *
from .utils import *

class Home(DataMixin, ListView):
    model = Equipment
    template_name = 'equipment/index.html'
    context_object_name = 'products'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items())) # общий словарь из содер контекста на базе listview + миксин из utils.py

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

class show_prod(DataMixin, DetailView):
    model = Equipment
    template_name = 'equipment/product.html'
    slug_url_kwarg = 'prod_slug'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['product'])
        return dict(list(context.items()) + list(c_def.items()))


class Category(DataMixin, ListView):
    model = Equipment
    template_name = 'equipment/index.html'
    context_object_name = 'products'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Продукт - " + str(context['products'][0].cat), cat_selected=context['products'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Equipment.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена:(</h1>')