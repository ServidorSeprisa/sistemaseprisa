from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    email = models.EmailField(max_length=50)
    birth = models.DateField(null=True,blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

from django.contrib.auth.models import AbstractUser
from django.db import models

class RegistroUsuario(AbstractUser):
    USER_TYPES = [
        ('admin', 'Administrador'),
        ('alm', 'Almacenista'),
        ('prod', 'Productor'),
        ('cal', 'Calidad'),
        ('entrada', 'Entrada')
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set', 
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions', 
        blank=True
    )

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

class Notificacion(models.Model):
    usuario = models.ForeignKey(RegistroUsuario, on_delete=models.CASCADE)
    TIPOS_USUARIO = [
        ('admin', 'Administrador'),
        ('entrada', 'Entrada'),
        ('alm', 'Almacenista'),
        ('prod', 'Productor'),
        ('cal', 'Calidad'),
    ]
    mensaje = models.TextField()
    leida = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificación para {self.usuario.username} - {self.mensaje[:20]}"



class FormatoRecepcionMateriaAlergenos(models.Model):

    fechaentrada = models.DateTimeField(auto_now_add=True)
    materiaprima = models.CharField(max_length=100, verbose_name='Materia Prima')
    loteseprisa = models.CharField(max_length=100, verbose_name="Lotes Seprisa")
    pesobruto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pesoneto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nocontenedores = models.IntegerField(null=True, blank=True)
    claveproveedor = models.CharField(max_length=10, null=True, blank=True)
    noanalisis = models.CharField(max_length=10, null=True, blank=True)
    sku = models.CharField(max_length=10, null=True, blank=True)
    noloteproveedor = models.CharField(max_length=10, null=True, blank=True)
    fechacaducidad = models.DateTimeField(null=True, blank=True)
    recibe = models.CharField(max_length=100, verbose_name='Recibe')

    def __str__(self) -> str:
        return self.materiaprima

class FormatoRecepcionMaterialEmpaque(models.Model):

    fechaentrada = models.DateTimeField(auto_now_add=True)
    material = models.CharField(max_length=100, verbose_name='Material')
    loteseprisa = models.CharField(max_length=100, verbose_name="Lotes Seprisa")
    pesobruto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pesoneto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nocontenedores = models.IntegerField(null=True, blank=True)
    claveproveedor = models.CharField(max_length=10, null=True, blank=True)
    noanalisis = models.CharField(max_length=10, null=True, blank=True)
    sku = models.CharField(max_length=10, null=True, blank=True)
    noloteproveedor = models.CharField(max_length=10, null=True, blank=True)
    recibe = models.CharField(max_length=100, verbose_name='Recibe')

    def __str__(self) -> str:
        return self.material

from django.db import models

class FormatoRecepcionMateriaPrima(models.Model):
    # fechaentrada = models.DateTimeField(auto_now_add=True)
    fechaentrada = models.DateField(null=True, blank=True)
    materiaprima = models.CharField(max_length=100, verbose_name='Materia Prima')
    loteseprisa = models.CharField(max_length=100, verbose_name="Lotes Seprisa")
    pesobruto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pesoneto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    nocontenedores = models.IntegerField(null=True, blank=True)
    cantidadneto = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    claveproveedor = models.CharField(max_length=10, null=True, blank=True)
    noanalisis = models.CharField(max_length=10, null=True, blank=True)
    sku = models.CharField(max_length=10, null=True, blank=True)
    noloteproveedor = models.CharField(max_length=10, null=True, blank=True)
    fechacaducidad = models.DateField(null=True, blank=True)
    recibe = models.CharField(max_length=100, verbose_name='Recibe')

    def __str__(self) -> str:
        return self.materiaprima

class EtiquetaIdentificacionMateriales(models.Model):
    material = models.CharField(max_length=100, verbose_name='Material', null=True, blank=True)
    noanalisis = models.CharField(max_length=100, verbose_name='No Analisis', null=True, blank=True)
    proveedorclientesku = models.CharField(max_length=100, verbose_name='Proveedor o Cliente SKU', null=True, blank=True)
    noloteproveedor = models.CharField(max_length=100, verbose_name='No Lote Proveedor', null=True, blank=True)
    noloteinterno = models.CharField(max_length=100, verbose_name='No Lote Interno', null=True, blank=True)
    pbruto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    ptara = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    pneto = models.CharField(max_length=100, verbose_name='P. Neto', null=True, blank=True)
    sku = models.CharField(max_length=100, verbose_name='SKU', null=True, blank=True)
    contenedor = models.CharField(max_length=100, null=True, verbose_name='Contenedor', blank=True)
    de = models.CharField(max_length=100, verbose_name='De', null=True, blank=True)
    realizo = models.CharField(max_length=100, verbose_name='Realizo', null=True, blank=True)
    verifico = models.CharField(max_length=100, verbose_name='Verifico', null=True, blank=True)

    formato_recepcion = models.ForeignKey(FormatoRecepcionMateriaPrima, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.formato_recepcion.materiaprima} - {self.material}"

class FormatoSolicitudAnalisis(models.Model):
    materiaprima = models.CharField(max_length=100, verbose_name='Materia Prima')
    productoterminado = models.CharField(max_length=100, verbose_name='Prodcuto Terminado')
    materialempaque = models.CharField(max_length=100, verbose_name='Material de Empaque')
    noanálisis = models.CharField(max_length=100, verbose_name='No. Analisis')
    fechahoraentrada = models.DateField(null=True,blank=True)
    nolote = models.CharField(max_length=100, verbose_name='No. Lote')
    cantidadrecibida = models.CharField(max_length=100, verbose_name='Cantidad Recibida')
    nocontenedores = models.CharField(max_length=100, verbose_name='No. Contenedores')
    producto = models.CharField(max_length=100, verbose_name='Producto')
    solicitante = models.CharField(max_length=100, verbose_name='Solicitante')
    recibe = models.CharField(max_length=100, verbose_name='Recibe')
    muestreo = models.CharField(max_length=100, verbose_name='Muetreo')
    fechahoramuestreo = models.CharField(max_length=100, verbose_name='Fecha y hora de muestreo')
    observaciones = models.CharField(max_length=100, verbose_name='Observaciones')
    analista = models.CharField(max_length=100, verbose_name='Analista')
    fechahoradictamen = models.DateField(null=True,blank=True)
    dictamen = models.CharField(max_length=100, verbose_name='Dictamen')
    observacioness = models.CharField(max_length=100, verbose_name='Observaciones')
    fechahoraentrega  = models.DateField(null=True,blank=True)

    def __str__(self) -> str:   
        return self.materiaprima
    
class EtiquetaCuarentena(models.Model):

    nombre = models.CharField(max_length=100,verbose_name='Nombre',null=True,blank=True)
    firma = models.CharField(max_length=100,verbose_name='Firma',null=True,blank=True)
    noanalisis = models.CharField(max_length=100, verbose_name='No. Analisis', null=True,blank=True)

    def __str__(self) -> str:
        return self.nombre

class KardexRecepcionMateriaPrimaAlmacen(models.Model):
    materiaprima = models.CharField(max_length=100, verbose_name='Materia Prima', null=True, blank=True)
    fechacaducidad = models.DateField(null=True, blank=True)
    fechaentrada = models.DateField(null=True, blank=True)
    codigoproveedorcliente = models.CharField(max_length=100, verbose_name='Codigo Proveedor o Cliente', null=True, blank=True)
    noloteseprisa = models.CharField(max_length=100, verbose_name='No. Lote Seprisa', null=True, blank=True)
    cantidadneto = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad Neto', null=True, blank=True)
    sku = models.CharField(max_length=100, verbose_name='SKU', null=True, blank=True)
    fechasalida = models.DateField(null=True, blank=True)
    clienteusointerno = models.CharField(max_length=100, verbose_name='Cliente Uso Interno', null=True, blank=True)
    noloteproveedor = models.CharField(max_length=100, verbose_name='No. Lote Proveedor', null=True, blank=True)
    cantidadsale = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad Sale', null=True, blank=True)
    cantidadqueda = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='Cantidad Queda', null=True, blank=True)
    realizo = models.CharField(max_length=100, verbose_name='Realizo', null=True, blank=True)
    observaciones = models.CharField(max_length=255, verbose_name='Observaciones', null=True, blank=True)
    formato_recepcion = models.ForeignKey(FormatoRecepcionMateriaPrima, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.formato_recepcion.materiaprima} - {self.materiaprima}"

class OrdenProduccion(models.Model):
    producto = models.CharField(max_length=100,verbose_name='Producto', null=True,blank=True)
    claveskumaquila = models.CharField(max_length=100,verbose_name='CLAVE/SKU Maquila', null=True,blank=True)
    presentacion = models.CharField(max_length=100,verbose_name='Presentacion', null=True,blank=True)
    noordenproduccion = models.CharField(max_length=100,verbose_name='No. Orden Produccion', null=True,blank=True)
    numerolote = models.CharField(max_length=100,verbose_name='Numero de lote', null=True,blank=True)
    fechacaducidad = models.DateField(null=True, blank=True)
    fechainicioproceso = models.DateField(null=True, blank=True)
    fechaterminoproceso = models.DateField(null=True, blank=True)
    rendimientoteorico = models.CharField(max_length=100,verbose_name='Rendimiento teorico', null=True,blank=True)
    rendimientoreal = models.CharField(max_length=100,verbose_name='Rendimiento real', null=True,blank=True)

    def __str__(self) ->str:
        return self.producto

class DetalleOrden(models.Model):
    orden = models.ForeignKey(OrdenProduccion, related_name='detalles', on_delete=models.CASCADE)
    skump = models.CharField(max_length=100,verbose_name='SKU MP', null=True,blank=True)
    material = models.CharField(max_length=100,verbose_name='Material', null=True,blank=True)
    nolote = models.CharField(max_length=100,verbose_name='No. Lpte', null=True,blank=True)
    unidad = models.CharField(max_length=100,verbose_name='Unidad', null=True,blank=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cantidad', null=True, blank=True)  # Cambiado a DecimalField
    surtio = models.CharField(max_length=100,verbose_name='Surtió', null=True,blank=True)
    verifico = models.CharField(max_length=100,verbose_name='Verificó', null=True,blank=True)
    observaciones = models.CharField(max_length=100,verbose_name='Observaciones',null=True,blank=True)

    def __str__(self) ->str:
        return self.skump
    
class FormatoBitacoraProductoTerminado(models.Model):
    fechaentrada = models.DateField(null=True, blank=True)
    producto = models.CharField(max_length=100, verbose_name='Materia Prima', null=True, blank=True)
    lote = models.CharField(max_length=100, verbose_name="Lotes Seprisa", null=True, blank=True)
    sku = models.CharField(max_length=100, verbose_name="sku", null=True, blank=True)
    presentacion = models.CharField(max_length=100, verbose_name="Presentacion", null=True, blank=True)
    contenedores = models.IntegerField(null=True, blank=True)
    cliente = models.CharField(max_length=10, null=True, blank=True)
    noanalisis = models.CharField(max_length=10, null=True, blank=True)
    fechacaducidad = models.DateField(null=True, blank=True)
    recibe = models.CharField(max_length=10, null=True, blank=True)
    observaciones = models.DateField(null=True, blank=True)

    def __str__(self) -> str:
        return self.producto

class Muestra(models.Model):
    orden_produccion = models.ForeignKey(OrdenProduccion, on_delete=models.CASCADE,null=True)
    noordenproduccion = models.CharField(max_length=100, default='NULL')  # Valor predeterminado aquí
    fila = models.IntegerField()
    columna = models.IntegerField()
    valor = models.FloatField()

    def save(self, *args, **kwargs):
        if not self.noordenproduccion:
            self.noordenproduccion = self.orden_produccion.noordenproduccion
        super().save(*args, **kwargs)

class Tabla(models.Model):
    orden_produccion = models.ForeignKey(OrdenProduccion, on_delete=models.CASCADE, related_name="tablas",null=True)
    tabla1_muestras = models.ManyToManyField(Muestra, related_name='tabla1', blank=True)
    tabla2_muestras = models.ManyToManyField(Muestra, related_name='tabla2', blank=True)

    def __str__(self):
        return f"Registro de Tablas {self.id} - Orden: {self.orden_produccion.noordenproduccion}"
