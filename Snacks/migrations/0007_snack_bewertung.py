# Generated by Django 4.1.3 on 2023-01-04 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Snacks', '0006_alter_snack_preis'),
    ]

    operations = [
        migrations.AddField(
            model_name='snack',
            name='bewertung',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=10),
        ),
    ]
