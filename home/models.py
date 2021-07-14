from django.db import models
from django.urls import reverse

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
    category = models.ManyToManyField(Category,blank=True)
    name = models.CharField(max_length=250)
    amount = models.PositiveIntegerField()
    unit_price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField(blank=True,null=True)
    total_price = models.PositiveIntegerField()
    information1 = models.TextField()
    information2 = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product')
    sku = models.CharField(max_length=150)
    available = models.BooleanField(default=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True)


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
    



