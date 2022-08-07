from rest_framework import serializers

from .models import (
    ProductCategory,
    Products,
    SubProducts
)


class ProductCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductCategory
        read_only_fields = ('id', )
        fields = read_only_fields + ('name', 'description')


class ProductsSerializer(serializers.ModelSerializer):

    category = ProductCategorySerializer()

    class Meta:
        model = Products
        read_only_fields = ('id', )
        fields = read_only_fields + ('name', 'category', 'description', 'image')


class SubProductsSerializer(serializers.ModelSerializer):

    product = ProductsSerializer()

    class Meta:
        model = SubProducts
        read_only_fields = ('id', )
        fields = read_only_fields + ('name', 'product', 'description', 'image')