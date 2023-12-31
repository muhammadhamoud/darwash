# Generated by Django 4.2 on 2023-09-22 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0002_services"),
    ]

    operations = [
        migrations.CreateModel(
            name="Projects",
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
                ("name", models.CharField(max_length=256)),
                ("discriptions", models.CharField(max_length=256)),
                ("image", models.FileField(blank=True, null=True, upload_to="")),
                ("icon", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "serices",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="services",
                        to="homepage.services",
                    ),
                ),
            ],
        ),
    ]
