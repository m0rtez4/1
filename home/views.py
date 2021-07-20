from django.shortcuts import render, get_object_or_404, redirect
from .models import MyUser, CommentForm, Comment, Category, Product, Variants, Images


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
    images = Images.objects.filter(product_id=id)
    comment_form = CommentForm()
    comment = Comment.objects.filter(product_id=id)
    similar = product.tags.similar_objects()[:2]
    if product.status != 'None' :
        if request.method == 'POST':
            variant = Variants.objects.filter(product_variant_id=id)
            var_id = request.POST.get('select')
            variants = Variants.objects.get(id=var_id)
        else:
            variant = Variants.objects.filter(product_variant_id=id)
            variants = Variants.objects.get(id=variant[0].id)

        context = {
            'product': product,
            'variant':variant,
            'variants':variants,
            'similar':similar,
            'comment_form':comment_form,
            'comment':comment,
            'images':images
        }
        return render(request, 'home/detail.html', context)
    else:

        context={
            'product':product,
            'similar': similar,
            'comment_form':comment_form,
            'comment':comment,
            'images': images
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