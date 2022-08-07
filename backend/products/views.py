from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import (
    ProductCategorySerializer,
    ProductsSerializer,
    SubProductsSerializer
)

from .models import (
    ProductCategory,
    Products,
    SubProducts
)

# Create your views here.
class SubproductsView(APIView):
    
    def get_queryset(self):
        return SubProducts.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = SubProducts.objects.all()
        serializer = SubProductsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsView(APIView):
    
    def get_queryset(self):
        return Products.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Products.objects.all()
        serializer = ProductsSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductCategoryView(APIView):
    
    def get_queryset(self):
        return ProductCategory.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = ProductCategory.objects.all()
        serializer = ProductCategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)