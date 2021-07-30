from django.shortcuts import render, redirect
from home.models import Product
from .models import *
from django.contrib.auth.decorators import login_required



def cart_detail(request):
    cart = Cart.objects.filter(user_id=request.user.id)
    total = 0
    for p in cart :
        if p.product.status != 'None':
            total += p.variant.total_price * p.quantity
        else:
            total += p.product.total_price * p.quantity
    context ={
        'cart':cart,
        'total':total
    }
    return render(request,'cart/cart.html',context)

@login_required(login_url='accounts:register_view')
def add_cart(request,id):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=id)
    if product.status != 'None':
        var_id = request.POST.get('select')
        data = Cart.objects.filter(user_id=request.user.id,variant_id=var_id)
        if data:
            check = 'yes'
        else:
            check = 'no'
    else:
        data = Cart.objects.filter(user_id=request.user.id,product_id=id)
        if data:
            check = 'yes'
        else:
            check = 'no'

    if request.method == 'POST':
        form = CartForm(request.POST)
        var_id = request.POST.get('select')
        if form.is_valid():
            info = form.cleaned_data['quantity']
            if check == 'yes':
                if product.status != 'None':
                    shop = Cart.objects.get(user_id=request.user.id,product_id=id,variant_id=var_id)
                else:
                    shop = Cart.objects.get(user_id=request.user.id,product_id=id)
                shop.quantity += info
                shop.save()
            else:
                Cart.objects.create(user_id=request.user.id,product_id=id,variant_id=var_id,quantity=info)
        return redirect(url)


@login_required(login_url='accounts:register_view')
def remove_cart(request,id):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.filter(id=id).delete()
    return redirect(url)


@login_required(login_url='accounts:register_view')
def remove_cart_all(request):
    url = request.META.get('HTTP_REFERER')
    Cart.objects.all().delete()
    return redirect(url)



