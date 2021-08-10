from django.db import models
from home.models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from django_jalali.db import models as jmodels





class Order(models.Model):
    SHOT = (
        ('در حال پردازش','در حال پردازش'),
        ('ارسال شده','ارسال شده')
    )
    SHOT1 =(
        ('a','پرداخت نشده'),
        ('b','بیانه پرداخت شده'),
        ('c','کامل پرداخت شده')
    )
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,verbose_name='کاربر')
    create = jmodels.jDateTimeField(auto_now_add=True,verbose_name='تاریخ ثیت سفارش')
    paid = models.CharField(max_length=30,choices=SHOT1,default='a',verbose_name='وضعیت پرداخت')
    f_name = models.CharField(max_length=300,verbose_name='نام')
    l_name = models.CharField(max_length=300,verbose_name='نام فامیلی')
    address = models.CharField(max_length=1000,verbose_name='آدرس')
    phone = models.CharField(max_length=11,verbose_name='شماره تماس')
    postal_code2 = models.PositiveIntegerField(blank=True, null=True,verbose_name='کد پستی')
    detail = models.TextField(blank=True,null=True,verbose_name='نظر کاربر')
    discount = models.PositiveIntegerField(blank=True,null=True,verbose_name='مقدار تخفیف')
    send = models.CharField(max_length=30,choices=SHOT,default='در حال پردازش',verbose_name='وضعیت ارسال' )
    code = models.CharField(max_length=100,blank=True,null=True,verbose_name='کد رهگیری')
    radio2 = models.CharField(max_length=20,blank=True,null=True,verbose_name='نحوه پرداخت')

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def __str__(self):
        return self.user.mobile

    def get_price(self):
        total = sum(i.price() for i in self.order_item.all())
        if self.discount:
            discount_price = (self.discount / 100) * total
            return int(total - discount_price)
        return total

    def get_price2(self):
        if self.radio2 == '4':
            return self.get_price()
        else:
            total = 15000
            return total












class ItemOrder(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_item',verbose_name='سبد سفارش')
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,verbose_name='کاربر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    variant = models.ForeignKey(Variants,on_delete=models.CASCADE,null=True,blank=True,verbose_name='ویژگی')
    quantity = models.IntegerField(verbose_name='تعداد سفارش')

    class Meta:
        verbose_name = 'سبد سفارش'
        verbose_name_plural = 'سبدهای سفارشات'


    def __str__(self):
        return self.user.mobile

    def size(self):
        return self.variant.size_variant.name

    def color(self):
        return self.variant.color_variant.name

    def price(self):
        if self.product.status != 'None':
            return self.variant.total_price * self.quantity
        else:
            return self.product.total_price * self.quantity




class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['f_name','l_name','phone','address','postal_code2','detail']



class Coupon(models.Model):
    code = models.CharField(max_length=100,unique=True,verbose_name='نام کد')
    active = models.BooleanField(default=False,verbose_name='فعال / غیرفعال')
    start = jmodels.jDateTimeField(verbose_name='تاریخ شروع تخفیف')
    end = jmodels.jDateTimeField(verbose_name='تاریخ پایان تخفیف')
    discount = models.IntegerField(verbose_name='مقدار تخفیف')

    class Meta:
        verbose_name = 'کوپن'
        verbose_name_plural = 'کوپن ها'


