from django.http import request
from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import Product
from webapp.models import Category


def detail_view(request, pk):
    product = get_object_or_404(Product,pk=pk)
    context = {'product': product}
    return render(request, 'detail.html', context=context)


def category_add_view(request):
    if request.method == "GET":
        return render(request, 'add_category.html')
    category_data = {
        'category_name': request.POST.get('category_name'),
        'category_description': request.POST.get('category_description'),
    }
    Category.objects.create(**category_data)
    return redirect('index_page')

def product_add_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, 'add_product.html', context={"categories": categories})
    product_data = {
        'product_name': request.POST.get('product_name'),
        'cost': request.POST.get('cost'),
        'image': request.POST.get('image'),
        'category_id': int(request.POST.get('category_id'))
    }
    Product.objects.create(**product_data)
    return redirect('index_page')

