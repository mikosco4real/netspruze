from itertools import product
from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'product_category'


class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'products'


class SubProducts(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        db_table = 'sub_products'