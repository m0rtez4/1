from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('verify/',views.verify,name='verify'),
    path('register/',views.register_view,name='register_view'),


]