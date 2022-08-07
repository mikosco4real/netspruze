from django.urls import path, include

from .views import (
    SubproductsView,
    ProductsView,
    ProductCategoryView
    )

app_name = 'products'

urlpatterns = [
    path('subproducts', SubproductsView.as_view(), name='subproducts'),
    path('', ProductsView.as_view(), name='products'),
    path('product_category', ProductCategoryView.as_view(), name='product_category'),
]