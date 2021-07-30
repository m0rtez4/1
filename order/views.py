from django.shortcuts import render, redirect
from .models import *


def order_detail(request):
    pass

def order_create(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            order = Order.objects.create(user_id=request.user.id,f_name=data['f_name'],l_name=data['l_name'],address=data['address'],phone=data['phone'],postal_code2=data['postal_code2'])
            return redirect('order:order_detail',order.id)
