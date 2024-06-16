from rest_framework import generics

from shop.filters import CategoryFilter, ProductFilter
from shop.models import Category, Product
from shop.serializers import CategoriesSerializer, ProductsSerializer


class CategoriesListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    filterset_class = CategoryFilter


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer


class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filterset_class = ProductFilter


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
