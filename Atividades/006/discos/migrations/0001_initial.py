# Generated by Django 4.2.6 on 2023-10-05 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Discos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=255)),
                ('descricao', models.TextField()),
                ('selo_fotografico', models.CharField(blank=True, max_length=255)),
                ('ano', models.DateTimeField(auto_now_add=True)),
                ('pais', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]
