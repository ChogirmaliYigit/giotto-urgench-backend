from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group, User
from unfold.admin import ModelAdmin, StackedInline

from shop.models import Category, Product

admin.site.unregister(User)
admin.site.unregister(Group)


@admin.register(User)
class UserAdmin(ModelAdmin, BaseUserAdmin):
    pass


@admin.register(Group)
class GroupAdmin(ModelAdmin, BaseGroupAdmin):
    pass


class ProductInline(StackedInline):
    model = Product
    fields = (
        "name",
        "category",
        "price",
        "image",
        "description",
    )
    extra = 1
    show_change_link = True
    show_full_result_count = True


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "name",
        "parent",
    )
    fields = list_display
    search_fields = list_display + ("id",)
    list_filter = ("parent",)
    inlines = [
        ProductInline,
    ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "parent":
            # Get the object ID from the URL if it's present
            object_id = request.resolver_match.kwargs.get("object_id")
            if object_id:
                # Exclude the current category from the queryset
                current_category = Category.objects.get(pk=object_id)
                kwargs["queryset"] = Category.objects.exclude(
                    id__in=[
                        *[
                            sub_category.pk
                            for sub_category in current_category.get_sub_categories()
                        ],
                        object_id,
                    ]
                )
            else:
                # If the object is new (no ID yet), show all categories
                kwargs["queryset"] = Category.objects.all()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = (
        "name",
        "category",
        "price",
    )
    fields = list_display + (
        "image",
        "description",
    )
    search_fields = fields
    list_filter = ("category",)
