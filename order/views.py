from django.shortcuts import render, redirect
from .models import *
from cart.models import Cart

def order_detail(request,order_id):
    order = Order.objects.get(id=order_id)
    context = {
        'order':order
    }
    return render(request,'order/order.html',context)

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.create(user_id=request.user.id,f_name=data['f_name'],l_name=data['l_name'],address=data['address'],phone=data['phone'],postal_code2=data['postal_code2'])
            cart = Cart.objects.filter(user_id=request.user.id)
            for c in cart:
                ItemOrder.objects.create(order_id=order.id,user_id=request.user.id,product_id=c.product_id,variant_id=c.variant_id,quantity=c.quantity)

            return redirect('order:order_detail',order.id)


