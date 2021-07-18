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
            'similar':similar
        }
        return render(request, 'home/detail.html', context)
    else:

        context={
            'product':product,
            'similar': similar
        }
        return render(request,'home/detail.html',context)