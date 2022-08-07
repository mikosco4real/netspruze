from django.contrib import admin

from .models import (
    ProductCategory,
    Products,
    SubProducts
)
# Register your models here.

admin.site.register((ProductCategory, Products, SubProducts))