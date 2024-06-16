from django.conf import settings
from rest_framework import serializers

from shop.models import Category, Product


class CategoriesSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = f"{settings.BACKEND_DOMAIN}{instance.image.url}"
        data["parent"] = (
            CategoriesSerializer(instance.parent).data if instance.parent else None
        )
        return data

    class Meta:
        model = Category
        fields = (
            "id",
            "name",
            "parent",
            "image",
        )


class ProductsSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["image"] = f"{settings.BACKEND_DOMAIN}{instance.image.url}"
        data["category"] = CategoriesSerializer(instance.category).data
        return data

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "price",
            "image",
            "description",
        )
