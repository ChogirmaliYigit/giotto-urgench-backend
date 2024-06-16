from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="sub_categories",
    )

    def __str__(self):
        return self.name

    def get_sub_categories(self):
        sub_categories = []
        for sub_category in self.sub_categories.all():
            sub_categories.append(sub_category)
            sub_categories.extend(sub_category.get_sub_categories())
        return sub_categories

    class Meta:
        db_table = "categories"
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to="products/")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "products"
