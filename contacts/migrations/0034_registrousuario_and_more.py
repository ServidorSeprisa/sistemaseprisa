# Generated by Django 5.1.5 on 2025-02-05 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0033_alter_kardexrecepcionmateriaprimaalmacen_cantidadneto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre')),
                ('apellidopaterno', models.CharField(max_length=100, verbose_name='Apellido Paterno')),
                ('apellidomaterno', models.CharField(max_length=100, verbose_name='Apellido Materno')),
                ('tipousuario', models.CharField(choices=[('admin', 'Administrador'), ('admin2', 'Administrador2'), ('alm', 'Almacen'), ('prod', 'Produccion'), ('cal', 'calidad')], max_length=100, verbose_name='Tipo Usuario')),
                ('correo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Correo')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña')),
                ('confirmacioncontraseña', models.CharField(max_length=100, verbose_name='Confirmacion Contraseña')),
            ],
        ),
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
