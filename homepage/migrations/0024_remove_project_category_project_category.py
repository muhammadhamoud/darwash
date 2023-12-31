# Generated by Django 4.2 on 2023-09-23 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0023_remove_project_category_project_category"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="project",
            name="category",
        ),
        migrations.AddField(
            model_name="project",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="homepage.productcategory",
            ),
            preserve_default=False,
        ),
    ]
