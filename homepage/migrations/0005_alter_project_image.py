# Generated by Django 4.2 on 2023-09-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0004_rename_projects_project_rename_services_service"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="image",
            field=models.ImageField(default="", upload_to="uploads/"),
            preserve_default=False,
        ),
    ]
