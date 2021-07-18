from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager

class Category(models.Model):
    sub_category = models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='sub')
    sub_cat = models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='category',null=True,blank=True)
    slug = models.SlugField(allow_unicode=True,unique=True,null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    VARIANT = (
        ('None','none'),
        ('Size','size'),
        ('Color','color')
    )
    category = models.ManyToManyField(Category,blank=True)
    name = models.CharField(max_length=250)
    amount = models.PositiveIntegerField(blank=True, null=True)
    unit_price = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True,null=True)
    total_price = models.PositiveIntegerField()
    information1 = RichTextField()
    information2 = RichTextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product')
    sku = models.CharField(max_length=150)
    available = models.BooleanField(default=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True)
    status = models.CharField(null=True,blank=True,max_length=200,choices=VARIANT)
    tags = TaggableManager(blank=True)


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
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Variants(models.Model):
    name = models.CharField(max_length=200)
    product_variant = models.ForeignKey(Product,on_delete=models.CASCADE)
    size_variant = models.ForeignKey(Size,on_delete=models.CASCADE,blank=True,null=True)
    color_variant = models.ForeignKey(Color,on_delete=models.CASCADE,blank=True,null=True)
    amount = models.PositiveIntegerField(blank=True, null=True)
    unit_price = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    total_price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product/color/',default=True)


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
