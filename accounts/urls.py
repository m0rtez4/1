from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('verify/',views.verify,name='verify'),
    path('register/',views.register_view,name='register_view'),
    path('profile/',views.profile,name='profile'),
    path('profile/address/',views.address,name='address'),
    path('profile/favourite/',views.favourite,name='favourite'),
    path('profile/history/',views.history,name='history')


]