# Generated by Django 4.2 on 2023-09-22 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0008_category_post_delete_homeinfo_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductCategory",
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
                ("name", models.CharField(max_length=100)),
                (
                    "description_short",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("description", models.TextField(blank=True, null=True)),
                ("image", models.ImageField(upload_to="uploads/")),
            ],
        ),
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
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="homepage.productcategory",
                    ),
                ),
            ],
        ),
    ]