# Generated by Django 4.1.5 on 2023-01-14 15:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoppingcart', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoppingcartitem',
            name='menge',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]