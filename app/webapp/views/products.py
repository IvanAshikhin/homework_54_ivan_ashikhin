from django.http import request
from django.shortcuts import render, redirect

from webapp.models import Product
from webapp.models import Category


def detail_view(request):
    product_pk = request.GET.get('pk')
    product = Product.objects.get(pk=product_pk)
    context = {'product': product}
    return render(request, 'detail.html', context=context)


def category_add_view(request):
    if request.method == "GET":
        return render(request, 'add_category.html')
    article_data = {
        'category_name': request.POST.get('category_name'),
        'category_description': request.POST.get('category_description'),
    }
    category = Category.objects.create(**article_data)

