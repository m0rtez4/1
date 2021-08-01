from django.shortcuts import render, get_object_or_404, redirect
from .models import MyUser, CommentForm, Comment, Category, Product, Variants, Images
from .forms import SearchForm
from django.db.models import Q
from cart.models import *





def home(request):
    category = Category.objects.filter(sub_cat=False)
    form = SearchForm()
    context ={
        'category':category,
        'form':form
    }
    return render(request, 'home/home.html', context)





def all_product(request,slug=None):
    products = Product.objects.all()
    form = SearchForm()

    category =Category.objects.filter(sub_cat=False)
    if slug :
        data = get_object_or_404(Category,slug=slug)
        products = products.filter(category=data)
    context={
        'products':products,
        'category':category,
        'form':form

    }
    return render(request, 'home/product.html', context)






def product_detail(request,id=None,slug=None):
    product = get_object_or_404(Product,id=id)
    images = Images.objects.filter(product_id=id)
    comment_form = CommentForm()
    comment = Comment.objects.filter(product_id=id)
    cart_form = CartForm()
    is_favourite = False
    if product.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    similar = product.tags.similar_objects()[:2]
    if product.status != 'None' :
        if request.method == 'POST':
            var_id = request.POST.get('select')
            variants = Variants.objects.get(id=var_id)
            variant = Variants.objects.filter(product_variant_id=id)
            colors = Variants.objects.filter(product_variant_id=id,size_variant_id=variants.size_variant_id)
            size =Variants.objects.filter(product_variant_id=id).distinct('size_variant_id')

        else:
            variant = Variants.objects.filter(product_variant_id=id)
            variants = Variants.objects.get(id=variant[0].id)
            colors = Variants.objects.filter(product_variant_id=id,size_variant_id=variants.size_variant_id)
            size =Variants.objects.filter(product_variant_id=id).distinct('size_variant_id')

        context = {
            'product': product,
            'variant':variant,
            'variants':variants,
            'similar':similar,
            'comment_form':comment_form,
            'comment':comment,
            'images':images,
            'cart_form':cart_form,
            'colors':colors,
            'size':size,
            'is_favourite': is_favourite
        }
        return render(request, 'home/detail.html', context)
    else:

        context={
            'product':product,
            'similar': similar,
            'comment_form':comment_form,
            'comment':comment,
            'images': images,
            'cart_form':cart_form,
            'is_favourite': is_favourite
        }
        return render(request,'home/detail.html',context)


def product_comment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            Comment.objects.create(comment=data['comment'],user_id=request.user.id,product_id=id)
        return redirect(url)



def product_search(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['search']
            if data is not None :
                lookup = Q(name__iexact=data)|Q(name__icontains=data)|Q(category__name__icontains=data)
                products = products.filter(lookup,available=True).distinct()
            return render(request,'home/product.html',{'products':products,'form':form})
    else:
        form = SearchForm()
        return render(request,'home/product.html',{'products':products,'form':form})



def favourite_product(request,id,slug):
    url = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=id,slug=slug)
    is_favourite = False
    if product.favourite.filter(id=request.user.id).exists():
        product.favourite.remove(request.user)
        is_favourite = False
    else:
        product.favourite.add(request.user)
        is_favourite = True

    return redirect(url)


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        lastName = request.POST['lastName']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

    context={

    }
    return render(request,'home/contact.html',context)