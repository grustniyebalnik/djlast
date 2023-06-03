from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator

from .utils import *
from .forms import *


class Home(DataMixin, ListView):
    model = Equipment
    template_name = 'equipment/index.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items())) # общий словарь из содер контекста на базе listview + миксин из utils.py

    def get_queryset(self):
        return Equipment.objects.filter(is_published=True)


def about(request):
    contact_list = Equipment.objects.all()
    paginator = Paginator(contact_list, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'equipment/about.html', {'page_obj':page_obj, 'menu': menu, 'title': 'about'})


def contact(request):
    return HttpResponse("contact")


def add_page(request):
    return HttpResponse("contact")


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


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'equipment/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form): #автомат при регистрации авторизует
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'equipment/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена:(</h1>')