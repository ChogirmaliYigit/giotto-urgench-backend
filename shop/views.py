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

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["detail"] = True
        return context


class ProductsListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    filterset_class = ProductFilter


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["detail"] = True
        return context
