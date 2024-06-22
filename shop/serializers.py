from django.conf import settings
from django.db.models import Case, IntegerField, Value, When
from rest_framework import serializers

from shop.models import Category, Product


class CategoriesSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        data = super().to_representation(instance)
        detail = self.context.get("detail", False)
        sub_category = self.context.get("sub_category", False)
        if detail:
            data["products"] = ProductsSerializer(
                instance.products.annotate(
                    is_english=Case(
                        When(name__regex=r"^[a-zA-Z ]*$", then=Value(1)),
                        default=Value(0),
                        output_field=IntegerField(),
                    )
                ).order_by("-is_english", "name"),
                many=True,
            ).data
            data["sub_categories"] = CategoriesSerializer(
                instance.sub_categories.annotate(
                    is_english=Case(
                        When(name__regex=r"^[a-zA-Z ]*$", then=Value(1)),
                        default=Value(0),
                        output_field=IntegerField(),
                    )
                ).order_by("-is_english", "name"),
                many=True,
                context={"sub_category": True},
            ).data
        data["image"] = f"{settings.BACKEND_DOMAIN}{instance.image.url}"
        if not sub_category:
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
        detail = self.context.get("detail", False)
        data["image"] = f"{settings.BACKEND_DOMAIN}{instance.image.url}"
        if detail:
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
            "is_new",
        )
