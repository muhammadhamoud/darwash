# Generated by Django 4.2 on 2023-09-23 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0016_alter_feature_image_alter_service_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feature",
            name="discriptions",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="service",
            name="discriptions",
            field=models.TextField(),
        ),
    ]
