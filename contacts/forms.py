# forms.py
from django import forms

class EtiquetaForm(forms.Form):
    material = forms.CharField(label='Material', max_length=255)
    no_analisis = forms.CharField(label='No. Análisis', max_length=255)
    proveedor_cliente_sku = forms.CharField(label='Proveedor o cliente SKU', max_length=255)
    no_lote_proveedor = forms.CharField(label='No. Lote de Proveedor', max_length=255)
    no_lote_interno = forms.CharField(label='No. Lote Interno', max_length=255)
    peso_bruto = forms.DecimalField(label='P. Bruto', max_digits=10, decimal_places=2)
    peso_tara = forms.DecimalField(label='P. Tara', max_digits=10, decimal_places=2)
    peso_neto = forms.DecimalField(label='P. Neto', max_digits=10, decimal_places=2)
    sku = forms.CharField(label='SKU', max_length=255)
    contenedor = forms.CharField(label='Contenedor', max_length=255)
    realizado_por = forms.CharField(label='Realizó', max_length=255)
    verificado_por = forms.CharField(label='Verifico', max_length=255)
    # contenedor = forms.CharField(label='Contenedor', max_length=255) #agregado para la etiqueta
    # de = forms.CharField(label='De', max_length=255)
    # realizo = forms.CharField(label='Realizo',max_length=255)
    # verifico = forms.CharField(label='Verifico',max_length=255)



# sjdbjhsbd
# se agrego el dia viernes 06/09/2024