from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from coolsite import settings
from equipment.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('equipment.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = pageNotFound