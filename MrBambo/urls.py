from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from MrBambo import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace='home')),
    path('accounts/',include('accounts.urls',namespace='accounts'))
]



if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)