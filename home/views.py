from django.shortcuts import render

def home(request):
    context ={}
    return render(request, 'home/home.html', context)

def all_product(request):
    context={}
    return render(request, 'home/product.html', context)
