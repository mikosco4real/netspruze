from django.db import models

# Create your models here.
class ProductCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'product_category'
        verbose_name = 'product_category'
        verbose_name_plural = 'product_categories'
    
    def __str__(self) -> str:
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    def __str__(self) -> str:
        return self.name


class SubProducts(models.Model):
    name = models.CharField(max_length=50)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        db_table = 'sub_products'
        verbose_name = 'sub_product'
        verbose_name_plural = 'sub_products'
    
    def __str__(self) -> str:
        return self.name