# Generated by Django 4.1.3 on 2022-11-30 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Poster', related_query_name='Posters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_or_down', models.CharField(choices=[('U', 'up'), ('D', 'down')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snacks.comment')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Voter', related_query_name='Voters', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gewicht', models.IntegerField()),
                ('beschreibung', models.CharField(blank=True, max_length=1000)),
                ('pictures', models.ImageField(blank=True, null=True, upload_to='snack_pictures/')),
                ('artikelnummer', models.CharField(max_length=100)),
                ('preis', models.FloatField()),
                ('erstellungs_zeitstempel', models.DateTimeField(auto_now_add=True)),
                ('hersteller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Hersteller', related_query_name='Hersteller', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Snacks',
                'verbose_name_plural': 'Snacks',
                'ordering': ['erstellungs_zeitstempel', 'name'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='snack',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snacks.snack'),
        ),
    ]
