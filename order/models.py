from django.db import models
from home.models import *
from django.contrib.auth.models import User
from django.forms import ModelForm





class Order(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)
    f_name = models.CharField(max_length=300)
    l_name = models.CharField(max_length=300)
    address = models.CharField(max_length=1000)
    phone = models.CharField(max_length=11)
    postal_code2 = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return self.user.mobile

class ItemOrder(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_item')
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    variant = models.ForeignKey(Variants,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField()


    def __str__(self):
        return self.user.mobile

    def size(self):
        return self.variant.size_variant.name

    def color(self):
        return self.variant.color_variant.name



class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['f_name','l_name','phone','address','postal_code2']
