# Generated by Django 5.0.6 on 2024-06-16 14:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("description", models.TextField()),
                ("image", models.ImageField(upload_to="products/")),
                ("price", models.DecimalField(decimal_places=2, max_digits=12)),
            ],
            options={
                "db_table": "products",
            },
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                (
                    "parent",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="sub_categories",
                        to="shop.category",
                    ),
                ),
            ],
            options={
                "db_table": "categories",
            },
        ),
    ]
