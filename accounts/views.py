from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from . import forms
from django.contrib.auth.models import User
from . import helper
from .models import MyUser
from django.contrib import messages



def register_view(request):
    form = forms.RegisterForm
    if request.method == 'POST':
        try:
            if 'mobile' in request.POST :
                mobile = request.POST.get('mobile')
                user = MyUser.objects.get(mobile=mobile)
                #send
                otp =helper.get_random_otp()
                helper.send_otp(mobile,otp)
                user.otp = otp
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
                helper.send_otp(mobile, otp)
                user.otp = otp
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