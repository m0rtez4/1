from django.shortcuts import render , get_object_or_404
from .models import *
def home(request):
    category = Category.objects.filter(sub_cat=False)
    context ={
        'category':category
    }
    return render(request, 'home/home.html', context)

def all_product(request,slug=None):
    products = Product.objects.all()
    category =Category.objects.filter(sub_cat=False)
    if slug :
        data = get_object_or_404(Category,slug=slug)
        products = products.filter(category=data)
    context={
        'products':products,
        'category':category

    }
    return render(request, 'home/product.html', context)


def product_detail(request,id=None,slug=None):
    product = get_object_or_404(Product,id=id,slug=slug)
    context={
        'product':product
    }
    return render(request,'home/detail.html',context)