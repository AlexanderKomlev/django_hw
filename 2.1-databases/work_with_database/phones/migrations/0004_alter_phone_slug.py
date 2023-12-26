# Generated by Django 5.0 on 2023-12-24 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='URL'),
        ),
    ]
