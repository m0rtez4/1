from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from order.models import ItemOrder, Order
from home.models import Product
from . import forms
from django.contrib.auth.models import User
from . import helper
from .forms import UserProfile , UserAddress
from .models import MyUser
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register_view(request):
    form = forms.RegisterForm
    if request.method == 'POST':
        try:
            if 'mobile' in request.POST :
                mobile = request.POST.get('mobile')
                user = MyUser.objects.get(mobile=mobile)
                #send
                otp =helper.get_random_otp()
                # helper.send_otp(mobile,otp)
                user.otp = otp
                print(otp)
                #save otp
                user.save()
                request.session['user_mobile'] = user.mobile
                #redirect
                return HttpResponseRedirect(reverse('accounts:verify'))

        except MyUser.DoesNotExist:
            form = forms.RegisterForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                otp = helper.get_random_otp()
                # helper.send_otp(mobile, otp)
                user.otp = otp
                print(otp)
                user.is_active = False
                user.save()
                request.session['user_mobile'] = user.mobile
                #redirect
                return HttpResponseRedirect(reverse('accounts:verify'))
    return render(request,'accounts/register.html',{'form':form})

def verify(request):
    try :
        mobile = request.session.get('user_mobile')
        user = MyUser.objects.get(mobile = mobile)
        if request.method == 'POST':

            if not helper.check_otp_expiration(user.mobile):
                messages.error(request, 'مدت زمان وارد کردن کد به پایان رسیده است')
                return HttpResponseRedirect(reverse('accounts:register_view'))
            if request.POST.get('otp') :
                if user.otp != int(request.POST.get('otp')):
                    messages.error(request, 'کد وارد شده صحیح نمی باشد')
                    return HttpResponseRedirect(reverse('accounts:verify'))
                user.is_active = True
                user.save()
                login(request,user)
                return HttpResponseRedirect(reverse('accounts:profile'))

        return render(request, 'accounts/verify.html', {'mobile': mobile})
    except MyUser.DoesNotExist :
        messages.error(request, 'مشکلی به وجود آمده است ، لطفا دوباره تلاش کنید')
        return HttpResponseRedirect(reverse('accounts:register_view'))

@login_required(login_url='accounts:register_view')
def profile(request):
    user = MyUser.objects.get(id = request.user.id)

    edit_user_form = UserProfile(request.POST or None)

    if edit_user_form.is_valid():
        first_name = edit_user_form.cleaned_data.get('first_name')
        last_name = edit_user_form.cleaned_data.get('last_name')
        email = edit_user_form.cleaned_data.get('email')

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

    context = {
        'edit_user':edit_user_form,
        'user':user
    }
    return render(request,'accounts/profile.html',context)


@login_required(login_url='accounts:register_view')
def address(request):
    user = MyUser.objects.get(id=request.user.id)
    edit_user_form = UserAddress(request.POST or None)

    if edit_user_form.is_valid():
        address = edit_user_form.cleaned_data.get('address')
        postal_code = edit_user_form.cleaned_data.get('postal_code')


        user.address = address
        user.postal_code = postal_code

        user.save()

    context = {
        'edit_user': edit_user_form,
        'user': user
    }
    return render(request, 'accounts/address.html', context)


@login_required(login_url='accounts:register_view')
def favourite(request):
    user = MyUser.objects.get(id=request.user.id)
    product1 = user.fa_user.all()
    is_favourite = False
    if product1.filter(id=request.user.id).exists():
        is_favourite = True

    context ={
        'product1':product1,
        'is_favourite':is_favourite,

    }
    return render(request,'accounts/wishlist.html',context)


@login_required(login_url='accounts:register_view')
def history(request):
    data = ItemOrder.objects.filter(user_id= request.user.id)
    data1 = Order.objects.filter(user_id=request.user.id)
    context={
        'data':data,
        'data1':data1

    }
    return render(request,'accounts/history.html',context)