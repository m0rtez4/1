from django.urls import path
from . import views


app_name = 'order'
urlpatterns = [
    path('',views.order_detail,name='order_detail'),
    path('create/',views.order_create,name='order_create'),
]