from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('add_page/', add_page, name='add_product'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('product/<slug:prod_slug>', show_prod.as_view(), name='prod'),
    path('category/<slug:cat_slug>', Category.as_view(), name='category'),
]