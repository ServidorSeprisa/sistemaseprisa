from typing import Any
from django.shortcuts import render

from django.urls import reverse_lazy
from django.views import generic

from django.db.models import QuerySet

from formatorecepcionmateriaalergenos.models import FormatoRecepcionMateriaAlergenos

# Create your views here.

class FormatoRecepcionMateriaAlargenosView(generic.ListView):
    model = FormatoRecepcionMateriaAlergenos
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoRecepcionMateriaAlergenos                                                                                                                                                                                                                                                                                                                                                                                                                                                                           .objects.filter(name__icontains=q)

        return super().get_queryset() 


class FormatoRecepcionMateriaAlergenosCreateView(generic.CreateView):
    model = FormatoRecepcionMateriaAlergenos
    fields = ('fechaentrada', 'materiaprima', 'loteseprisa', 'pesobruto', 'pesoneto', 'nocontenedores', 'claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe')

class FormatoRecepcionMateriaAlergenosUpdateView(generic.UpdateView):
    model = FormatoRecepcionMateriaAlergenos
    fields = ('fechaentrada', 'materiaprima', 'loteseprisa', 'pesobruto', 'pesoneto', 'nocontenedores', 'claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe')
    # fields = ('avatar','name', 'email', 'birth','phone',)
    success_url = reverse_lazy('formatorecepcionmateriaalergenos_edit')

class FormatoRecepcionMateriaAlergenosDeleteView(generic.DeleteView):
    model = FormatoRecepcionMateriaAlergenos
    success_url = reverse_lazy('formatorecepcionmateriaalergenos_list')

def contacts(request):
    # Lógica de la vista
    return render(request, 'contacts/contacs_list.html')