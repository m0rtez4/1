from django.urls import path , include
from . import views

app_name ='cart'
urlpatterns = [
    path('',views.cart_detail,name='cart_detail'),
    path('next/',views.cart,name='cart'),
    path('add/<int:id>/',views.add_cart,name='add_cart'),
    path('remove/<int:id>/',views.remove_cart,name='remove_cart'),
    path('removeall/',views.remove_cart_all,name='remove_cart_all')
]