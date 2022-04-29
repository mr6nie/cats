from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from .yasg import urlpatterns as yasg

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/cats/', include('apps.cat.urls'))
]

urlpatterns += yasg

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)