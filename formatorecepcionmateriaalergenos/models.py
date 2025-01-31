from django.db import models

# Create your models here.
    
class FormatoRecepcionMateriaAlergenos(models.Model):
    
    fechaentrada = models.DateTimeField(auto_now_add=True)
    materiaprima = models.CharField(max_length=100, verbose_name='Materia Prima')
    loteseprisa = models.CharField(max_length=100, verbose_name="Lotes Seprisa")
    pesobruto = models.CharField(max_length=10, null=True, blank=True)
    pesoneto = models.CharField(max_length=10, null=True, blank=True)
    nocontenedores = models.CharField(max_length=10, null=True, blank=True)
    claveproveedor = models.CharField(max_length=10, null=True, blank=True)
    noanalisis = models.CharField(max_length=10, null=True, blank=True)
    sku = models.CharField(max_length=10, null=True, blank=True)
    noloteproveedor = models.CharField(max_length=10, null=True, blank=True)
    fechacaducidad = models.DateTimeField()
    recibe = models.CharField(max_length=100, verbose_name='Recibe')

    def __str__(self) -> str:
        return self.materiaprima
