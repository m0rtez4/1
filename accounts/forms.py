from django import forms
from . import models


class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['mobile',]

class UserProfile(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['first_name','last_name','email',]

class UserAddress(forms.ModelForm):
    class Meta:
        model = models.MyUser
        fields = ['address','postal_code']