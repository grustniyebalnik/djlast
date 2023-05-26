from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add_page/', addpage, name='add_product'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('product/<int:prod_id>', show_prod, name='prod'),
    path('category/<int:cat_id>', show_category, name='category'),
]