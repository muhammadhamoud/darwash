# Generated by Django 4.2 on 2023-09-22 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("homepage", "0011_teammember_testimonial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="testimonial",
            name="date_published",
        ),
    ]
