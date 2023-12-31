# Generated by Django 4.2 on 2023-09-22 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Banner",
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
                ("image", models.URLField()),
                ("title", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Blurb",
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
                ("title", models.CharField(max_length=256)),
                ("content", models.TextField()),
                ("link", models.CharField(max_length=256)),
                ("link_text", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="HomeInfo",
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
                ("tagline", models.CharField(max_length=256)),
                ("example_email", models.EmailField(max_length=254)),
                ("email_button", models.CharField(max_length=256)),
            ],
        ),
    ]
