# Generated by Django 5.1 on 2024-10-03 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0016_alter_ordenproduccion_noordenproduccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordenproduccion',
            old_name='noordenproduccion',
            new_name='nordenproduccion',
        ),
        migrations.AlterField(
            model_name='detalleorden',
            name='nolote',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='No. Lote'),
        ),
    ]
