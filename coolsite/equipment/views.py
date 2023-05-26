from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


from .models import *

menu = ["about", "Добавить статью", "Обратная связь", "Войти"]

def index(request):
    products = Equipment.objects.all()
    return render(request, 'equipment/index.html', {'products': products, 'menu': menu, 'title': 'main page'})

def about(request):
    return render(request, 'equipment/about.html', {'menu': menu, 'title': 'about'})

def archive(request, year):
    if int(year) > 2023:
        return redirect('home')
    return HttpResponse(f"<h1>archive</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена:(</h1>')