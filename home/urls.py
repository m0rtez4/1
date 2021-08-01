from django.contrib import admin
from django.urls import path
from . import views

app_name ='home'
urlpatterns = [
    path('',views.home,name='home'),
    path('product/',views.all_product,name='product'),
    path('detail/<int:id>/<slug>/',views.product_detail,name ='detail'),
    path('category/<slug>/',views.all_product,name='category'),
    path('comment/<int:id>/',views.product_comment,name='product_comment'),
    path('search/',views.product_search,name='product_search'),
    path('favourite/<int:id>/<slug>/',views.favourite_product,name='favourite'),
    path('contact/',views.contact,name='contact'),
    path('contact/create/',views.contact_create,name='contact_create'),


]