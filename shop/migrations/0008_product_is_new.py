# Generated by Django 5.0.6 on 2024-06-22 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0007_alter_category_image_alter_product_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_new",
            field=models.BooleanField(default=False),
        ),
    ]
