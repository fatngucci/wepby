# Generated by Django 3.1.3 on 2020-12-11 06:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useradmin', '0002_auto_20201127_1632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2000, 12, 11)),
        ),
    ]
