from django.db import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Категория')
    category_description = models.TextField(max_length=2000, null=True, blank=False, verbose_name="Описание категории")

    def __str__(self):
        return f'{self.category_name} {self.category_description}'


class Product(models.Model):
    product_name = models.CharField(max_length=1000, null=False, blank=False, verbose_name='Название продукта')
    category = models.ForeignKey(to=Category, null=False, blank=False, related_name='products',
                                 on_delete=models.RESTRICT, verbose_name='Категория')
    add_date = models.DateTimeField(auto_now=True,verbose_name='Дата добавления')
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    image = models.TextField(max_length=10000,null=False,blank=False,verbose_name='Ссылка изображения')

    def __str__(self):
        return f'{self.product_name} {self.category} {self.add_date} {self.cost}'
