
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from django import forms
from django_jalali.db import models as jmodels
from accounts.models import MyUser



class Category(models.Model):
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub',verbose_name='زیر دسته بندی')
    sub_cat = models.BooleanField(default=False,verbose_name='زیر دسته بندی می باشد / نمی باشد')
    name = models.CharField(max_length=200,verbose_name='نام دسته بندی')
    create = jmodels.jDateField(auto_now_add=True,verbose_name='تاریخ ساخت دسته بندی')
    update = jmodels.jDateField(auto_now=True,verbose_name='آخرین بروزرسانی')
    image = models.ImageField(upload_to='category',null=True,blank=True,verbose_name='عکس دسته بندی')
    slug = models.SlugField(allow_unicode=True,unique=True,null=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'



class Product(models.Model):
    VARIANT = (
        ('None','none'),
        ('Size','size'),
        ('Color','color'),
        ('Both','Both')
    )

    name = models.CharField(max_length=250,verbose_name='نام محصول')
    amount = models.PositiveIntegerField(blank=True, null=True,verbose_name='تعداد محصول')
    unit_price = models.PositiveIntegerField(blank=True, null=True,verbose_name='قیمت اصلی')
    discount = models.PositiveIntegerField(blank=True,null=True,verbose_name='مقدار تخفیف')
    total_price = models.PositiveIntegerField(verbose_name='قیمت نهایی')
    information1 = RichTextField(verbose_name='توضیحات کوتاه محصول')
    information2 = RichTextField(verbose_name='توضیحات تکمیلی محصول')
    create = jmodels.jDateField(auto_now_add=True,verbose_name='تاریح ثیت محصول')
    update = jmodels.jDateField(auto_now=True,verbose_name='تاریخ آخرین بروزرسانی')
    image = models.ImageField(upload_to='product',verbose_name='عکس محصول')
    category = models.ManyToManyField(Category, blank=True, verbose_name='دسته بندی')
    sku = models.CharField(max_length=150)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True,verbose_name='آدرس url')
    tags = TaggableManager(blank=True,verbose_name='تگ ها')
    favourite = models.ManyToManyField(MyUser,blank=True,related_name='fa_user',verbose_name='مورد علاقه ی کاربران')
    available = models.BooleanField(default=True, verbose_name='موجود / ناموجود')
    status = models.CharField(null=True, blank=True, max_length=200, choices=VARIANT, verbose_name='وضعیت ویژگی')

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


    def get_absolute_url(self):
        return reverse('home:detail',args=[self.id,self.slug])



    def __str__(self):
        return self.name


    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price)/100
            return int(self.unit_price - total)
        return self.total_price
    


class Size(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام سایز')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'سایز'
        verbose_name_plural = 'سایزها'


class Color(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام رنگ')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'رنگ'
        verbose_name_plural = 'رنگ ها'


class Variants(models.Model):
    name = models.CharField(max_length=200,verbose_name='نام محصول دارای ویژگی')
    product_variant = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='اضافه کردن ویژگی برای کدام محصول')
    size_variant = models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True,verbose_name='سایز')
    color_variant = models.ForeignKey(Color,on_delete=models.CASCADE,blank=True,null=True,verbose_name='رنگ')
    amount = models.PositiveIntegerField(blank=True, null=True,verbose_name='تعداد')
    unit_price = models.PositiveIntegerField(blank=True, null=True,verbose_name='قیمت اصلی')
    discount = models.PositiveIntegerField(blank=True, null=True,verbose_name='مقدار تخفیف')
    total_price = models.PositiveIntegerField(verbose_name='قیمت با تخفیف')
    image = models.ImageField(upload_to='product/color/',default=True,verbose_name='عکس محصول دارای ویژگی')

    class Meta:
        verbose_name = 'ویژگی'
        verbose_name_plural = 'ویژگی ها'


    def __str__(self):
        return self.name


    @property
    def total_price(self):
        if not self.discount:
            return self.unit_price
        elif self.discount:
            total = (self.discount * self.unit_price)/100
            return int(self.unit_price - total)
        return self.total_price

class Comment(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE,verbose_name='کاربر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='نظر برای محصول')
    comment = models.TextField(verbose_name='نظر')
    create = jmodels.jDateField(auto_now_add=True,verbose_name='تاریخ نظر')
    reply = RichTextField(blank=True,verbose_name='پاسخ به نظر')
    is_active = models.BooleanField(default=False,verbose_name='نظر نمایش داده شود / نشود')
    is_reply = models.BooleanField(default=False,verbose_name='پاسخ نمایش داده شود / نشود')

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'

    def __str__(self):
        return self.product.name

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]
        widgets = {
            'comment': forms.Textarea(attrs={'class':'form-control form-control--sm textarea--height-200','placeholder':'پیام'})
        }
        labels={
            'comment':''
        }

class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    image = models.ImageField(upload_to='gallery/',blank=True,verbose_name='عکس های محصول')

    class Meta:
        verbose_name = 'عکس'
        verbose_name_plural = 'عکس ها'