from django_filters import rest_framework as filters

from shop.models import Category, Product


class CategoryFilter(filters.FilterSet):
    name = filters.CharFilter("name", lookup_expr="icontains")
    parent_id = filters.CharFilter("parent__pk")

    class Meta:
        model = Category
        fields = ["name", "parent_id"]


class ProductFilter(filters.FilterSet):
    name = filters.CharFilter("name", lookup_expr="icontains")
    category_id = filters.CharFilter("category__pk")
    price = filters.NumberFilter(field_name="price")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    description = filters.CharFilter("description", lookup_expr="icontains")

    class Meta:
        model = Product
        fields = [
            "name",
            "category_id",
            "price",
            "description",
        ]
