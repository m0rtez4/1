from django.db import models
from home.models import *
from django.forms import ModelForm


class Cart(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,verbose_name='کاربر')
    variant = models.ForeignKey(Variants,on_delete=models.CASCADE,null=True,blank=True,verbose_name='ویژگی')
    quantity = models.PositiveIntegerField(verbose_name='تعداد')

    def __str__(self):
        return self.user.mobile

    class Meta:
        verbose_name = 'سبد خرید'
        verbose_name_plural = 'سبدهای خرید'



class CartForm(ModelForm):
    class Meta:
        model = Cart
        fields = ['quantity']
