from django.urls import path

from webapp.views.base import index_view

from webapp.views.products import category_add_view, detail_view

urlpatterns = [
    path("", index_view, name="index_page"),
    path('product/', detail_view),
    path('categories/add', category_add_view, name='category_add'),
]
