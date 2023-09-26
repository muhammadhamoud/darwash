# Generated by Django 4.2 on 2023-09-23 22:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0019_remove_project_serices_project_category_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="category",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="categories",
                to="homepage.productcategory",
            ),
        ),
    ]