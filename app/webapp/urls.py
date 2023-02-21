from django.urls import path
from webapp.views.base import index_view
from webapp.views.products import category_add_view, detail_view, product_add_view

urlpatterns = [
    path("", index_view, name="index_page"),
    path('products/<int:pk>', detail_view, name ='details'),
    path('categories/add', category_add_view, name='category_add'),
    path('product/add', product_add_view, name='product_add'),
]
