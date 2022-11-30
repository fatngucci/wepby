# Generated by Django 4.1.3 on 2022-11-30 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Snacks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='pictures',
            field=models.ImageField(blank=True, null=True, upload_to='snack_pictures/'),
        ),
        migrations.AlterField(
            model_name='snack',
            name='preis',
            field=models.FloatField(),
        ),
    ]