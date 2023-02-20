from django.contrib import admin

from webapp.models import Category, Product


# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name', 'category_description')
    list_filter = ('id', 'category_name', 'category_description')
    search_fields = ('id', 'category_name')
    fields = ('category_name', 'category_description')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'add_date', 'cost', 'image', 'description')
    list_filter = ('id', 'product_name', 'category', 'add_date', 'cost', 'image', 'description')
    search_fields = ('id', 'product_name', 'category')
    fields = ('product_name', 'category', 'add_date', 'cost')
    readonly_fields = ('id', 'image', 'add_date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
