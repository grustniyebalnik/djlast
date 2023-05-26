
from django.contrib import admin
from django.urls import path, include

from equipment.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('equipment.urls'))
]

handler404 = pageNotFound