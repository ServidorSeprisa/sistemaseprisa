# Generated by Django 5.1 on 2024-08-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_formatorecepcionmaterialempaque_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formatorecepcionmateriaalergenos',
            name='fechacaducidad',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formatorecepcionmateriaalergenos',
            name='nocontenedores',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formatorecepcionmateriaalergenos',
            name='pesobruto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='formatorecepcionmateriaalergenos',
            name='pesoneto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='formatorecepcionmaterialempaque',
            name='nocontenedores',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='formatorecepcionmaterialempaque',
            name='pesobruto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='formatorecepcionmaterialempaque',
            name='pesoneto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
