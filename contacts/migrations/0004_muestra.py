# Generated by Django 5.1.5 on 2025-02-28 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_registrousuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Muestra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fila', models.IntegerField()),
                ('columna', models.IntegerField()),
                ('valor', models.FloatField()),
            ],
        ),
    ]
