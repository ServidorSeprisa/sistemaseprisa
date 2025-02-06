# Generated by Django 5.1.5 on 2025-02-06 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0038_registrousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='cantidadneto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad Neto'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='cantidadqueda',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad Queda'),
        ),
        migrations.AlterField(
            model_name='kardexrecepcionmateriaprimaalmacen',
            name='cantidadsale',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Cantidad Sale'),
        ),
    ]
