from django.db.models import Case, IntegerField, Value, When
from rest_framework import generics

from shop.filters import CategoryFilter, ProductFilter
from shop.models import Category, Product
from shop.serializers import CategoriesSerializer, ProductsSerializer


class CategoriesListView(generics.ListAPIView):
    serializer_class = CategoriesSerializer
    filterset_class = CategoryFilter

    def get_queryset(self):
        queryset = (
            Category.objects.filter(parent__isnull=True)
            .annotate(
                is_english=Case(
                    When(name__regex=r"^[a-zA-Z ]*$", then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
            )
            .order_by("-is_english", "name")
        )
        return queryset


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["detail"] = True
        return context


class ProductsListView(generics.ListAPIView):
    serializer_class = ProductsSerializer
    filterset_class = ProductFilter

    def get_queryset(self):
        queryset = Product.objects.annotate(
            is_english=Case(
                When(name__regex=r"^[a-zA-Z ]*$", then=Value(1)),
                default=Value(0),
                output_field=IntegerField(),
            )
        ).order_by("-is_english", "name")
        return queryset


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["detail"] = True
        return context
