from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from MrBambo import settings
from azbankgateways.urls import az_bank_gateways_urls
from order.views import go_to_gateway_view,callback_gateway_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace='home')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('cart/',include('cart.urls',namespace='cart')),
    path('order/',include('order.urls',namespace='order')),
    path('bankgateways/', az_bank_gateways_urls()),
    path('go-to-gateway/',go_to_gateway_view),
    path('callback-gateway/',callback_gateway_view),
]



if settings.DEBUG:
    # add root static files
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # add media static files
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)