# Generated by Django 5.0 on 2023-12-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0004_alter_phone_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(),
        ),
    ]