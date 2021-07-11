from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django import forms

from accounts.myusermanager import MyUserManager


class MyUser(AbstractUser):
    username = None
    mobile = models.CharField(max_length=11,unique=True)
    address = models.TextField(blank=True)
    postal_code = models.PositiveIntegerField(blank=True,null=True)
    otp = models.PositiveIntegerField(blank=True,null=True)
    otp_create_time = models.DateTimeField(auto_now=True)

    objects = MyUserManager()
    USERNAME_FIELD = 'mobile'
    REQUIRED_FIELDS = []
    backend = 'accounts.mybackend.MobileBackend'

