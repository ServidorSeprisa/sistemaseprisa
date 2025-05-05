from typing import Any
from django.shortcuts import render, redirect

from django.urls import reverse_lazy
from django.views import generic

from django.db.models import QuerySet

from django.views import View

from contacts.models import Contact
from contacts.models import FormatoRecepcionMateriaAlergenos
from contacts.models import FormatoRecepcionMaterialEmpaque
from contacts.models import FormatoRecepcionMateriaPrima
from contacts.models import EtiquetaIdentificacionMateriales
from contacts.models import OrdenProduccion
from contacts.models import DetalleOrden
from contacts.models import FormatoBitacoraProductoTerminado
from contacts.models import FormatoSolicitudAnalisis
from contacts.models import KardexRecepcionMateriaPrimaAlmacen
from contacts.models import RegistroUsuario

from django.views.generic.detail import DetailView

from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import RegistroUsuarioCreationForm
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'contacts/home.html')

def menu_principal(request):
    return render(request, 'contacts/menu_principal.html')

def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect(assign_dashboard(user)) 
    else:
        form = RegistroUsuarioCreationForm()
    return render(request, 'contacts/register.html', {'form': form})

def assign_dashboard(user):
    """ Asigna la vista del dashboard según el tipo de usuario """
    dashboard_urls = {
        'admin': 'menu_admin',
        'alm': 'menu_almacen',
        'prod': 'menu_produccion',
        'cal': 'menu_calidad',
        'entrada': 'menu_entrada'
    }
    return dashboard_urls.get(user.user_type, 'home')  

from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

class LoginView(LoginView):
    template_name = 'contacts/login.html'

    def form_valid(self, form):
        """ Redirige al menú según el tipo de usuario autenticado """
        usuario = form.get_user()
        login(self.request, usuario) 

        print(f"Usuario autenticado: {usuario.username} - Tipo: {usuario.user_type}")  

        dashboard_urls = {
            'admin': 'menu_admin',
            'alm': 'menu_almacen',
            'prod': 'menu_produccion',
            'cal': 'menu_calidad',
            'entrada': 'menu_entrada'
        }

        redirect_url = dashboard_urls.get(usuario.user_type, 'home')

        return redirect(redirect_url)

from django.views.generic import ListView

class UserListView(ListView):
    model = RegistroUsuario
    template_name = 'contacts/registro_usuarios_list.html'  
    context_object_name = 'usuarios'


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RegistroUsuario
from .forms import RegistroUsuarioCreationForm  

class UserEditView(UpdateView):
    model = RegistroUsuario
    form_class = RegistroUsuarioCreationForm
    template_name = 'contacts/registro_usuarios_edit.html'
    success_url = reverse_lazy('registro_usuarios_list')  

from django.views.generic import DeleteView

class UserDeleteView(DeleteView):
    model = RegistroUsuario
    template_name = 'contacts/registro_usuarios_confirm_delete.html'
    success_url = reverse_lazy('registro_usuarios_list')

@login_required
def menu_admin(request):
    return render(request, 'contacts/menu_admin.html')

@login_required
def menu_entrada(request):
    return render(request, 'contacts/menu_entrada.html')

@login_required
def menu_produccion(request):
    return render(request, 'contacts/menu_produccion.html')

from django.shortcuts import render
from .models import Notificacion

@login_required
def menu_almacen(request):
    return render(request, 'contacts/menu_almacen.html')

@login_required
def menu_calidad(request):
    return render(request, 'contacts/menu_calidad.html')

class ContactListView(generic.ListView):
    model = Contact
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return Contact.objects.filter(name__icontains=q)

        return super().get_queryset() 


class ContactCreateView(generic.CreateView): 
    model = Contact 
    fields = ('name', 'email', 'birth','phone',)
    success_url = reverse_lazy('contact_list')

class ContactUpdateView(generic.UpdateView):
    model = Contact
    fields = ('name', 'email', 'birth', 'phone',)
    success_url = reverse_lazy('contact_list')

class ContactDeleteView(generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contact_list')

class Menu(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu.html')

class MenuAdmin(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_admin.html')  
     
class MenuEntrada(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_entrada.html')     
     
class MenuAlmacen(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_almacen.html')     

class MenuProduccion(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_produccion.html')     

class MenuCalidad(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_calidad.html')    

class MenuPAdmin(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_p_admin.html')  
     
class MenuPEntrada(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_p_entrada.html')     
     
class MenuPAlmacen(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_p_almacen.html')     

class MenuPProduccion(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_p_produccion.html')     

class MenuPCalidad(View):   
     def get(self, request, *args, **kwargs):
     	return render(request, 'contacts/menu_p_calidad.html')   
     
# FORMATO RECEPCION MATERIA ALERGENOS -------------------------------
     
class FormatoRecepcionMateriaAlergenosView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_recepcion_materia.html')

from django.views.generic import ListView
    
class FormatoRecepcionMateriaAlergenosListView(ListView):
    model = FormatoRecepcionMateriaAlergenos
    template_name = 'contacts/formato_recepcion_materia.html'
    context_object_name = "object_list"
    paginate_by = 15  

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(materiaprima__icontains=query) |
                Q(loteseprisa__icontains=query) |
                Q(claveproveedor__icontains=query)
            )
        return queryset

from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import FormatoRecepcionMateriaPrima
from django.db.models import Q

def formato_recepcion_material_alergenos_list(request):
    query = request.GET.get("q", "")
    page = int(request.GET.get("page", 1))
    items_per_page = 15
    start = (page - 1) * items_per_page
    end = start + items_per_page

    queryset = FormatoRecepcionMateriaAlergenos.objects.filter(
        Q(materiaprima__icontains=query) |
        Q(claveproveedor__icontains=query)
    )[start:end]
    
    table_html = render_to_string("partials/formato_recepcion_table_body.html", {"object_list": queryset})
    
    return JsonResponse({
        "table_body": table_html,
        "has_next": len(queryset) == items_per_page, 
        "has_previous": page > 1
    })

class FormatoRecepcionMateriaAlergenosCreateView(generic.CreateView):
    model = FormatoRecepcionMateriaAlergenos 
    fields = ('materiaprima','loteseprisa','pesobruto','pesoneto','nocontenedores','claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe',)

    success_url = reverse_lazy('formatorecepcionmateriaalergenos_list')
    template_name='contacts/formato_recepcion_materia_alergenos_form.html'

class FormatoRecepcionMateriaAlergenosUpdateView(generic.UpdateView):
    model = FormatoRecepcionMateriaAlergenos
    fields = ('materiaprima','loteseprisa','pesobruto','pesoneto','nocontenedores','claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe')
    success_url = reverse_lazy('formatorecepcionmateriaalergenos_list')
    template_name='contacts/formato_recepcion_materia_alergenos_form.html'

class FormatoRecepcionMateriaAlergenosDeleteView(generic.DeleteView):
    model = FormatoRecepcionMateriaAlergenos
    success_url = reverse_lazy('formatorecepcionmateriaalergenos_list')
    template_name='contacts/formato_recepcion_materia_alergenos_confirm_delete.html'

class FormatoRecepcionMateriaAlergenosListViewView(generic.ListView):
    model = FormatoRecepcionMateriaAlergenos
    paginate_by = 15
    template_name = 'contacts/formato_recepcion_materia_alergenos_view.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoRecepcionMateriaAlergenos.objects.filter(materiaprima__icontains=q)
        return super().get_queryset()

# FORMATO RECEPCION MATERIAL EMPAQUE --------------------------------

class FormatoRecepcionMaterialEmpaqueView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_recepcion_material_empaque.html')
    
from django.views.generic import ListView
    
class FormatoRecepcionMaterialEmpaqueListView(ListView):
    model = FormatoRecepcionMaterialEmpaque
    template_name = 'contacts/formato_recepcion_material_empaque.html'
    context_object_name = "object_list"
    paginate_by = 15  

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(material__icontains=query) |
                Q(loteseprisa__icontains=query) |
                Q(claveproveedor__icontains=query)
            )
        return queryset

from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import FormatoRecepcionMaterialEmpaque
from django.db.models import Q

def formato_recepcion_material_empaque_list(request):
    query = request.GET.get("q", "")
    page = int(request.GET.get("page", 1))
    items_per_page = 15
    start = (page - 1) * items_per_page
    end = start + items_per_page

    queryset = FormatoRecepcionMaterialEmpaque.objects.filter(
        Q(materiaprima__icontains=query) |
        Q(claveproveedor__icontains=query)
    )[start:end]
    
    table_html = render_to_string("partials/formato_recepcion_table_body.html", {"object_list": queryset})
    
    return JsonResponse({
        "table_body": table_html,
        "has_next": len(queryset) == items_per_page,  
        "has_previous": page > 1
    })

class FormatoRecepcionMaterialEmpaqueCreateView(generic.CreateView):
    model = FormatoRecepcionMaterialEmpaque
    fields = ('material','loteseprisa','pesobruto','pesoneto','nocontenedores','claveproveedor','noanalisis','sku','noloteproveedor','recibe',)

    success_url = reverse_lazy('formatorecepcionmaterialempaque_list')
    template_name='contacts/formato_recepcion_material_empaque_form.html'

class FormatoRecepcionMaterialEmpaqueUpdateView(generic.UpdateView):
    model = FormatoRecepcionMaterialEmpaque
    fields = ('material','loteseprisa','pesobruto','pesoneto','nocontenedores','claveproveedor','noanalisis','sku','noloteproveedor','recibe',)
    success_url = reverse_lazy('formatorecepcionmaterialempaque_list')
    template_name='contacts/formato_recepcion_material_empaque_form.html'

class FormatoRecepcionMaterialEmpaqueDeleteView(generic.DeleteView):
    model = FormatoRecepcionMaterialEmpaque
    success_url = reverse_lazy('formatorecepcionmaterialempaque_list')
    template_name='contacts/formato_recepcion_material_empaque_confirm_delete.html'


class FormatoRecepcionMaterialEmpaqueListViewView(generic.ListView):
    model = FormatoRecepcionMaterialEmpaque
    paginate_by = 15
    template_name = 'contacts/formato_recepcion_material_empaque_view.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoRecepcionMaterialEmpaque.objects.filter(material__icontains=q)
        return super().get_queryset()

# FORMATO RECEPCION MATERIA PRIMA ------------------------------------------------------

class FormatoRecepcionMateriaPrimaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_recepcion_materia_prima.html')


class FormatoRecepcionMateriaPrimaListViewView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/pruebatabla_view.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=q)
        return super().get_queryset()
    
class FormatoRecepcionMateriaPrimaListView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/formato_recepcion_materia_prima.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=q)
        return super().get_queryset()
    
from django.views.generic import ListView
from .models import FormatoRecepcionMateriaPrima
from django.db.models import Q
class PruebaTablaView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/pruebatabla.html')
    
class PruebaTablaListView(ListView):
    model = FormatoRecepcionMateriaPrima
    template_name = 'contacts/pruebatabla.html'
    context_object_name = "object_list"
    paginate_by = 15  

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(materiaprima__icontains=query) |
                Q(loteseprisa__icontains=query) |
                Q(claveproveedor__icontains=query)
            )
        return queryset

from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import FormatoRecepcionMateriaPrima
from django.db.models import Q

def formato_recepcion_list(request):
    query = request.GET.get("q", "")
    page = int(request.GET.get("page", 1))
    items_per_page = 15
    start = (page - 1) * items_per_page
    end = start + items_per_page

    queryset = FormatoRecepcionMateriaPrima.objects.filter(
        Q(materiaprima__icontains=query) |
        Q(claveproveedor__icontains=query)
    )[start:end]
    
    table_html = render_to_string("partials/formato_recepcion_table_body.html", {"object_list": queryset})
    
    return JsonResponse({
        "table_body": table_html,
        "has_next": len(queryset) == items_per_page,  
        "has_previous": page > 1
    })

class FormatoRecepcionMateriaPrimaCreateView(generic.CreateView):
    model = FormatoRecepcionMateriaPrima
    fields = ('materiaprima', 'loteseprisa', 'pesobruto', 'pesoneto', 'nocontenedores','cantidadneto', 'claveproveedor', 'noanalisis', 'sku', 'noloteproveedor', 'fechacaducidad', 'recibe')
    success_url = reverse_lazy('formato_recepcion_list')
    template_name = 'contacts/formato_recepcion_materia_prima_form.html'

    def get_initial(self):
        initial_data = super().get_initial()
        for field in self.fields:
            value = self.request.GET.get(field)
            if value:
                initial_data[field] = value
        return initial_data

    def form_valid(self, form):
        return super().form_valid(form)

class FormatoRecepcionMateriaPrimaUpdateView(generic.UpdateView):
    model = FormatoRecepcionMateriaPrima
    fields = ('materiaprima','loteseprisa','pesobruto','pesoneto','nocontenedores','cantidadneto','claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe')
    success_url = reverse_lazy('formato_recepcion_list')
    template_name='contacts/formato_recepcion_materia_prima_form.html'

class FormatoRecepcionMateriaPrimaDeleteView(generic.DeleteView):
    model = FormatoRecepcionMateriaPrima
    success_url = reverse_lazy('formato_recepcion_list')
    template_name='contacts/formato_recepcion_materia_prima_confirm_delete.html'

    
# ETIQUETAS IDENTIFICACION MATERIALES ---------------------------------------------
class EtiquetaIdentificacionMaterialesView(View):
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q', '')
        etiquetas = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=search_query) if search_query else FormatoRecepcionMateriaPrima.objects.all()

        id = request.GET.get('id')
        etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, id=id) if id else None

        context = {
            'etiquetas': etiquetas,
            'etiqueta': etiqueta,
        }
        return render(request, 'contacts/etiqueta_identificacion_materiales.html', context)

class EtiquetaIdentificacionMaterialesListView(generic.ListView):
    model = EtiquetaIdentificacionMateriales
    template_name = 'contacts/etiqueta_identificacion_materiales.html'  # Cambia esto al nombre de tu plantilla

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return Contact.objects.filter(name__icontains=q)

        return super().get_queryset() 
    
    
class EtiquetaIdentificacionMaterialesCreateView(generic.CreateView): 
    model = EtiquetaIdentificacionMateriales
    fields = ('material','noanalisis','proveedorclientesku','noloteproveedor','noloteinterno','pbruto','ptara','pneto','sku','contenedor','de','realizo','verifico',)
    success_url = reverse_lazy('etiqueta_identificacion_materiales')

class etiquetas(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/etiqueta_identificacion_materiales.html')

def buscar_etiqueta_identificacion_materiales(request):
    etiqueta = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        etiqueta = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=query).first()
    
    return render(request, 'contacts/etiqueta_identificacion_materiales.html', {'etiqueta': etiqueta})

class GuardarEtiquetaView(View):
    def post(self, request, *args, **kwargs):
        formato_id = request.POST.get('id')
        formato_recepcion = get_object_or_404(FormatoRecepcionMateriaPrima, id=formato_id)

        etiqueta = EtiquetaIdentificacionMateriales(
            material=formato_recepcion.materiaprima,
            noanalisis=formato_recepcion.noanalisis,
            proveedorclientesku=formato_recepcion.claveproveedor,
            noloteproveedor=formato_recepcion.noloteproveedor,
            noloteinterno=formato_recepcion.loteseprisa,
            pbruto=formato_recepcion.pesobruto,
            pneto=formato_recepcion.pesoneto,
            sku=formato_recepcion.sku,
            de=formato_recepcion.nocontenedores,
            ptara=request.POST.get('ptara'),
            contenedor=request.POST.get('contenedor'),
            realizo=request.POST.get('realizo'),
            verifico=request.POST.get('verifico'),
        )
        etiqueta.save()
        try:
            etiqueta.save()
        except Exception as e:
            print("Error al guardar la etiqueta:", e)
        return redirect('etiquetas')
    
class orden_produccion(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/orden_produccion.html')
    
class orden_produccion2(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/orden_produccion2.html')

from django.shortcuts import get_object_or_404

def tu_vista_guardar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        if id:
            etiqueta = get_object_or_404(EtiquetaIdentificacionMateriales, id=id)
        else:
            etiqueta = EtiquetaIdentificacionMateriales()

        materia_prima = request.POST.get('material')
        recepcion = FormatoRecepcionMateriaPrima.objects.filter(materiaprima=materia_prima).first()

        if recepcion:
            etiqueta.material = recepcion.materiaprima
            etiqueta.proveedorclientesku = recepcion.claveproveedor
            etiqueta.noloteproveedor = recepcion.noloteproveedor
            etiqueta.noloteinterno = recepcion.loteseprisa 
            etiqueta.sku = recepcion.sku

        etiqueta.noanalisis = request.POST.get('no_analisis')
        etiqueta.pbruto = request.POST.get('pbruto')
        etiqueta.ptara = request.POST.get('ptara')
        etiqueta.pneto = request.POST.get('pneto')
        etiqueta.contenedor = request.POST.get('contenedor')
        etiqueta.de = request.POST.get('de')
        etiqueta.realizo = request.POST.get('realizo')
        etiqueta.verifico = request.POST.get('verifico')

        etiqueta.save()
        return redirect('listar_etiquetas')  

    return redirect('buscar_etiqueta') 

# ETIQUETA CUARENTENA -------------------------------------------------------

class Etiqueta_cuarentena(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/etiqueta_cuarentena.html')

class EtiquetaCuarentenaView(View):
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q', '')
        if search_query:
            etiquetas = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=search_query)
        else:
            etiquetas = FormatoRecepcionMateriaPrima.objects.all()
        
        id = request.GET.get('id')
        etiqueta = None
        if id:
            etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, id=id)
        
        context = {
            'etiquetas': etiquetas,
            'etiqueta': etiqueta,
        }
        return render(request, 'contacts/etiqueta_identificacion_materiales.html', context)    

class GuardarEtiquetaCuarentenaView(View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        data = {
            'materiaprima': request.POST.get('material'),
            'noanalisis': request.POST.get('no_analisis'),
            'firma': request.POST.get('firma'),
        }

        if id:
            etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, id=id)
            for key, value in data.items():
                setattr(etiqueta, key, value)
            etiqueta.save()
        else:
            FormatoRecepcionMateriaPrima.objects.create(**data)
        
        return redirect('tu_vista_listado')
    
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        data = {
            'nombre': request.POST.get('nombre'),
            'noanalisis': request.POST.get('no_analisis'),
            'firma': request.POST.get('firma'),
        }

        if id:
            etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, id=id)
            for key, value in data.items():
                setattr(etiqueta, key, value)
            etiqueta.save()
        else:
            FormatoRecepcionMateriaPrima.objects.create(**data)
        
        return redirect('tu_vista_listado')
        
class ListadoEtiquetaCuarentenaView(View):
    def get(self, request, *args, **kwargs):
        etiquetas = FormatoRecepcionMateriaPrima.objects.all()
        return render(request, 'contacts/etiqueta_cuarentena_list.html', {'etiquetas': etiquetas})

# FORMATO SOLICITUD ANALISIS -------------------------------------------------

class FormatoSolicitudAnalisisView(View): 
    def get(self, request, *args, **kwargs):
        search_query = request.GET.get('q', '')
        if search_query:
            etiquetas = FormatoSolicitudAnalisis.objects.filter(materiaprima__icontains=search_query)
        else:
            etiquetas = FormatoSolicitudAnalisis.objects.all()
        
        id = request.GET.get('id')
        etiqueta = ' '
        if id:
            etiqueta = get_object_or_404(FormatoSolicitudAnalisis, id=id)
        
        context = {
            'etiquetas': etiquetas,
            'etiqueta': etiqueta,
        }
        return render(request, 'contacts/formato_solicitud_analisis.html', context)

class Formato_solicitud_analisis(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_solicitud_analisis.html')

def buscar_solicitud_analisis(request):
    etiqueta = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        etiqueta = FormatoSolicitudAnalisis.objects.filter(materiaprima__icontains=query).first()
    
    return render(request, 'contacts/formato_solicitud_analisis.html', {'etiqueta': etiqueta})

class GuardarSolicitudAnalisisView(View):
    def post(self, request, *args, **kwargs):
        id = request.POST.get('id')
        data = {
            'materiaprima': request.POST.get('materiaprima'),
            'productoterminado': request.POST.get('productoterminado'),
            'materialempaque': request.POST.get('materialempaque'),
            'noanalisis': request.POST.get('noanalisis'),
            'fechahoraentrada': request.POST.get('fechahoraentrada'),
            'nolote': request.POST.get('nolote'),
            'cantidadrecibida': request.POST.get('cantidadrecibida'),
            'nocontenedores': request.POST.get('nocontenedores'),
            'producto': request.POST.get('producto'),
            'solicitante': request.POST.get('solicitante'),
            'recibecc': request.POST.get('recibecc'),
            'muestreo': request.POST.get('muestreo'),
            'fechahoramuestreo': request.POST.get('fechahoramuestreo'),
            'observaciones': request.POST.get('observaciones'),
            'analista': request.POST.get('analista'),
            'fechahoradictamen': request.POST.get('fechahoradictamen'),
            'dictamen': request.POST.get('dictamen'),
            'aprobado': request.POST.get('aprobado'),
            'rechazado': request.POST.get('rechazado'),
            'observaciones': request.POST.get('observaciones'),
            'fechahoraentregaresultados': request.POST.get('fechahoraentregaresultados'),
            'enteradoresultado': request.POST.get('enteradoresultado'),
        }

        if id:
            etiqueta = get_object_or_404(FormatoSolicitudAnalisis, id=id)
            for key, value in data.items():
                setattr(etiqueta, key, value)
            etiqueta.save()
        else:
            FormatoSolicitudAnalisis.objects.create(**data)
        
        return redirect('tu_vista_listado')

class ListadoSolicitudAnalisisView(View):
    def get(self, request, *args, **kwargs):
        etiquetas = FormatoSolicitudAnalisis.objects.all()
        return render(request, 'contacts/formato_solicitud_analisis_list.html', {'etiquetas': etiquetas})
    


from django.http import JsonResponse 
from .models import FormatoRecepcionMateriaPrima

def get_materia_prima_details(request):
    query = request.GET.get('materiaprima', '')
    if query:
        try:
            item = FormatoRecepcionMateriaPrima.objects.get(materiaprima=query)
            data = {
                'materiaprima': item.materiaprima,
                'proveedor': item.proveedor,  
                'sku': item.sku,              
                'lote_interno': item.lote_interno,  
                'lote_proveedor': item.lote_proveedor,  
            }
            return JsonResponse(data)
        except FormatoRecepcionMateriaPrima.DoesNotExist:
            return JsonResponse({'error': 'No se encontró el registro'}, status=404)
    return JsonResponse({'error': 'No se proporcionó un nombre de materia prima'}, status=400)

# EXPORTAR DOCUMENTOS PDF ----------------------------------------------

from django.template.loader import get_template
from django.http import HttpResponse
from xhtml2pdf import pisa
from io import BytesIO

def export_contacts_pdf(request):
    contacts = Contact.objects.all()
    
    template_path = 'contacts/contacts_pdf.html'
    context = {'contacts': contacts}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contacts.pdf"'

    result = BytesIO()
    pisa_status = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)
    
    if pisa_status.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_etiqueta_identificacion_materiales_pdf(request):
    etiquetas = EtiquetaIdentificacionMateriales.objects.all()[:15]
    
    template_path = 'contacts/etiqueta_identificacion_materiales_pdf.html'
    context = {'etiquetas': etiquetas}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="EtiquetaIdentificacionMateriales.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import FormatoRecepcionMateriaPrima

def descargar_etiqueta(request, pk):
    material = get_object_or_404(FormatoRecepcionMateriaPrima, pk=pk)

    contenedores = material.nocontenedores
    etiquetas = []
    for i in range(1, contenedores + 1):
        etiqueta = {
            'material': material.materiaprima,
            'no_analisis': material.noanalisis,
            'proveedor': material.claveproveedor,
            'lote_proveedor': material.noloteproveedor,
            'lote_interno': material.loteseprisa,
            'peso_bruto': material.pesobruto,
            'peso_neto': material.pesoneto,
            'sku': material.sku,
            'fechacaducidad': material.fechacaducidad,
            'contenedor': i,
            'de': contenedores,
            
        }
        etiquetas.append(etiqueta)

    template_path = 'contacts/etiqueta_identificacion_materiales_pdf.html'
    context = {'etiquetas': etiquetas}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="etiquetas_{material.materiaprima}.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_etiqueta_cuarentena_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/etiqueta_cuarentena_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="EtiquetaCuarentena.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return 

def export_formato_solicitud_analisis_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:1]
    
    template_path = 'contacts/formato_solicitud_analisis_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="FormatoSolicitudAnalisis.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

from django.http import JsonResponse, HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import json
from io import BytesIO

def export_formato_recepcion_materia_prima_pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_ids = data.get('ids', [])

        if not selected_ids:
            return JsonResponse({"error": "No IDs provided"}, status=400)

        objects = FormatoRecepcionMateriaPrima.objects.filter(pk__in=selected_ids)

        template_path = 'contacts/formato_recepcion_materia_prima_pdf.html'
        context = {'FormatoRecepcionMateriaPrimax': objects}

        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="FormatoRecepcionMateriaPrima.pdf"'

        result = BytesIO()
        pisa_status = pisa.CreatePDF(
            BytesIO(html.encode("UTF-8")),
            dest=result,
            encoding='UTF-8'
        )

        if pisa_status.err:
            return HttpResponse('Error generando el PDF', status=500)

        response.write(result.getvalue())
        return response

    return JsonResponse({"error": "Invalid request"}, status=400)


def export_formato_recepcion_material_empaque_pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_ids = data.get('ids', [])

        if not selected_ids:
            return JsonResponse({"error": "No IDs provided"}, status=400)

        objects = FormatoRecepcionMaterialEmpaque.objects.filter(pk__in=selected_ids)

        template_path = 'contacts/formato_recepcion_material_empaque_pdf.html'
        context = {'FormatoRecepcionMaterialEmpaquex': objects}

        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="FormatoRecepcionMaterialEmpaque.pdf"'

        result = BytesIO()
        pisa_status = pisa.CreatePDF(
            BytesIO(html.encode("UTF-8")),
            dest=result,
            encoding='UTF-8'
        )

        if pisa_status.err:
            return HttpResponse('Error generando el PDF', status=500)

        response.write(result.getvalue())
        return response

    return JsonResponse({"error": "Invalid request"}, status=400)

def export_formato_recepcion_materia_alergenos_pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_ids = data.get('ids', [])

        if not selected_ids:
            return JsonResponse({"error": "No IDs provided"}, status=400)

        objects = FormatoRecepcionMateriaAlergenos.objects.filter(pk__in=selected_ids)

        template_path = 'contacts/formato_recepcion_materia_alergenos_pdf.html'
        context = {'FormatoRecepcionMateriaAlergenosx': objects}

        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="FormatoRecepcionMateriaAlergenos.pdf"'

        result = BytesIO()
        pisa_status = pisa.CreatePDF(
            BytesIO(html.encode("UTF-8")),
            dest=result,
            encoding='UTF-8'
        )

        if pisa_status.err:
            return HttpResponse('Error generando el PDF', status=500)

        response.write(result.getvalue())
        return response

    return JsonResponse({"error": "Invalid request"}, status=400)

from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from .models import OrdenProduccion  

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import OrdenProduccion 

def export_orden_produccion_pdf(request):
    ordenes = OrdenProduccion.objects.all()[:15]

    if not ordenes.exists():
        return HttpResponse("No hay órdenes de producción disponibles", status=404)

    template_path = 'contacts/orden_produccion_pdf.html' 
    context = {'ordenes': ordenes}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="OrdenProduccion.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(html, dest=result)

    if pdf.err:
        return HttpResponse(f'Error generando el PDF: {pdf.err}', status=500)

    response.write(result.getvalue()) 
    return response

def export_ordenes_produccion_pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_ids = data.get('ids', [])

        if not selected_ids:
            return JsonResponse({"error": "No IDs provided"}, status=400)

        objects = OrdenProduccion.objects.filter(pk__in=selected_ids)

        template_path = 'contacts/ordenes_produccion_pdf.html'
        context = {'OrdenesProduccionx': objects}

        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="OrdenesProduccion.pdf"'

        result = BytesIO()
        pisa_status = pisa.CreatePDF(
            BytesIO(html.encode("UTF-8")),
            dest=result,
            encoding='UTF-8'
        )

        if pisa_status.err:
            return HttpResponse('Error generando el PDF', status=500)

        response.write(result.getvalue())
        return response

    return JsonResponse({"error": "Invalid request"}, status=400)

def export_orden_produccion2_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/orden_produccion2_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="OrdendeProduccion2.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO
from .models import OrdenProduccion, DetalleOrden

def export_orden_produccion_create_listview_pdf(request):
    orden = OrdenProduccion.objects.last()
    if not orden:
        return HttpResponse("No hay órdenes de producción disponibles", status=404)

    detalles = DetalleOrden.objects.filter(orden=orden)

    context = {
        'OrdenProduccion': orden,
        'object_list': detalles
    }

    template_path = 'contacts/orden_produccion_create_listview_pdf.html'
    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="OrdenProduccion.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(html, dest=result)

    if pdf.err:
        return HttpResponse(f'Error generando el PDF: {pdf.err}', status=500)

    response.write(result.getvalue())
    return response



from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def export_kardex_pdf(request):
    query = request.GET.get('q')
    etiqueta = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=query).first()
    salidas = KardexRecepcionMateriaPrimaAlmacen.objects.filter(formato_recepcion=etiqueta) if etiqueta else []

    template_path = 'contacts/kardex_pdf.html'
    context = {
        'etiqueta': etiqueta,
        'salidas': salidas,
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="kardex_report.pdf"'

    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error al generar el PDF')
    return response


# ORDEN DE PRODUCCION ----------------------------------------------------------------

class OrdenProduccionView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/orden_produccion.html')
    
class OrdenProduccionCreateView(generic.CreateView): 
    def get(self, request):
        return render(request, 'contacts/orden_produccion.html')

    def post(self, request):
        data = {
            'producto': request.POST.get('producto'),
            'claveskumaquila': request.POST.get('clavesku_maquila'),
            'presentacion': request.POST.get('presentacion'),
            'noordenproduccion': request.POST.get('noorden_produccion'),
            'numerolote': request.POST.get('numero_lote'),
            'fechacaducidad': request.POST.get('fecha_caducidad'),
            'fechainicioproceso': request.POST.get('fechainicio_proceso'),
            'fechaterminoproceso': request.POST.get('fechatermino_proceso'),
            'rendimientoteorico': request.POST.get('rendimiento_teorico'),
            'rendimientoreal': request.POST.get('rendimiento_real'),
        }

        OrdenProduccion.objects.create(**data)

        return redirect('ordenproduccion_view')    
    
class OrdenProduccionListView(generic.ListView):
    model = DetalleOrden
    paginate_by = 5
    template_name = 'contacts/orden_produccion.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return DetalleOrden.objects.filter(material__icontains=q)
        
        return super().get_queryset() 

class OrdenProduccionCreateListView(generic.CreateView):
    model = DetalleOrden 
    fields = ('orden', 'skump', 'material', 'nolote', 'unidad', 'cantidad', 'surtio', 'verifico')
    success_url = reverse_lazy('ordenproduccion_list')
    template_name = 'contacts/formato_recepcion_materia_prima_form.html'

class DetalleOrdenUpdateView(generic.UpdateView):
    model = DetalleOrden
    fields = ('skump', 'material', 'nolote', 'unidad','cantidad','surtio','verifico',)
    success_url = reverse_lazy('ordenproduccion_list')
    template_name='contacts/orden_produccion_form.html'

class DetalleOrdenDeleteView(generic.DeleteView):
    model = DetalleOrden
    success_url = reverse_lazy('ordenproduccion_list')
    template_name='contacts/orden_produccion_form.html'



def buscar_orden_produccion(request):
 
    OrdenProduccion = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        OrdenProduccion = OrdenProduccion.objects.filter(noordenproduccion__icontains=query).first()
    
    return render(request, 'contacts/orden_produccion.html', {'OrdenProduccion': OrdenProduccion})

def buscar_material(request):
    OrdenProduccion = ' '
    if 'q' in request.GET:
        query = request.GET['q']
        OrdenProduccion = OrdenProduccion.objects.filter(material__icontains=query).first()
    
    return render(request, 'contacts/orden_produccion.html', {'OrdenProduccion': OrdenProduccion})

class DetalleOrdenCreateView(generic.CreateView): 
    def get(self, request):
        return render(request, 'contacts/orden_produccion.html')

    def post(self, request):
        data = {
            'skump': request.POST.get('skump'),
            'material': request.POST.get('material'),
            'nolote': request.POST.get('no_lote'),
            'unidad': request.POST.get('unidad'),
            'cantidad': request.POST.get('cantidad'),
            'surtio': request.POST.get('surtio'),
            'verifico': request.POST.get('verifico'),
            'observaciones': request.POST.get('observaciones'),
        }

        OrdenProduccion.objects.create(**data)

        return redirect('orden_produccion_view')    
    
class DetalleOrdenListView(generic.ListView):
    model = DetalleOrden
    paginate_by = 5
    template_name = 'contacts/orden_produccion.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return DetalleOrden.objects.filter(material__icontains=q)
        
        return super().get_queryset() 

class DetalleOrdenCreateListView(generic.CreateView):
    model = DetalleOrden 
    fields = ('orden', 'skump', 'material', 'nolote', 'unidad', 'cantidad', 'surtio', 'verifico')
    success_url = reverse_lazy('ordenproduccion_list')
    template_name = 'contacts/formato_recepcion_materia_prima_form.html'

def orden_produccion_view(request):
    return render(request, 'orden_produccion.html')


def OrdenProduccionList(request):
    return render(request, 'orden_produccion_list.html')


class OrdenProduccionList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/orden_produccion_list.html')
    
class OrdenProduccionListViewView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/orden_produccion_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        queryset = FormatoRecepcionMateriaPrima.objects.all()

        if q:
            queryset = queryset.filter(materiaprima__icontains=q)

        queryset = queryset.prefetch_related('kardexrecepcionmateriaprimaalmacen_set')

        return queryset
    
from django.views import generic
from django.db.models import Q
from .models import FormatoRecepcionMateriaPrima, OrdenProduccion

class OrdenProduccionListViewViewV(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/orden_produccion_list_2.html'

    def get_queryset(self):
        """Filtra los datos según los criterios de búsqueda"""
        q = self.request.GET.get('q', '').strip()
        search_noorden = self.request.GET.get('search_noorden', '').strip()

        queryset = FormatoRecepcionMateriaPrima.objects.all()

        if q:
            queryset = queryset.filter(materiaprima__icontains=q)

        queryset = queryset.prefetch_related('kardexrecepcionmateriaprimaalmacen_set')

        return queryset

    def get_context_data(self, **kwargs):
        """Pasa datos adicionales al template"""
        context = super().get_context_data(**kwargs)
        search_noorden = self.request.GET.get('search_noorden', '').strip()

        orden_produccion = None
        if search_noorden:
            orden_produccion = OrdenProduccion.objects.filter(noordenproduccion=search_noorden).first()

        context.update({
            'search_noorden': search_noorden,
            'OrdenProduccion': orden_produccion,  
        })

        return context
from django.shortcuts import render

def chat_room(request):
    return render(request, 'contacts/chat.html')

class OrdenProduccionListListView(generic.ListView):
    model = OrdenProduccion
    paginate_by = 15
    template_name = 'contacts/orden_produccion_list_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        queryset = OrdenProduccion.objects.all()

        if q:
            queryset = queryset.filter(noordenproduccion__icontains=q)
        return queryset

class OrdenProduccionUpdateView(generic.UpdateView):
    model = OrdenProduccion
    fields = ('producto','claveskumaquila','presentacion','noordenproduccion','numerolote','fechacaducidad','fechainicioproceso','fechaterminoproceso','rendimientoteorico','rendimientoreal')
    success_url = reverse_lazy('orden_produccion_list_view')
    template_name='contacts/orden_produccion_form.html'

class OrdenProduccionDeleteView(generic.DeleteView):
    model = OrdenProduccion
    success_url = reverse_lazy('orden_produccion_list_view')
    template_name='contacts/orden_produccion_confirm_delete.html'

class OrdenProduccionListViewV(generic.ListView):
    model = OrdenProduccion
    paginate_by = 15
    template_name = 'contacts/orden_produccion_list_list_view.html'
    context_object_name = "object_list"

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(producto=query) |
                Q(claveskumaquila=query) |
                Q(numerolote=query) |
                Q(noordenproduccion=query)
            )
        return queryset

class OrdenProduccionListList(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/orden_produccion_create.html')
    
    
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import OrdenProduccion, DetalleOrden
import json

import json
from django.http import JsonResponse
from django.shortcuts import render
from .models import OrdenProduccion, DetalleOrden

import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from .models import OrdenProduccion, DetalleOrden, FormatoRecepcionMateriaPrima
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import generic
from .models import OrdenProduccion, DetalleOrden, FormatoRecepcionMateriaPrima

from django.db import transaction
from django.http import JsonResponse
import json
from django.http import HttpResponseBadRequest
import json

from django.contrib.auth import get_user_model
from django.contrib import messages
import json

from django.contrib.auth import get_user_model
from django.contrib import messages
import json
from decimal import Decimal, InvalidOperation

RegistroUsuario = get_user_model() 

@login_required
def ordenproduccion_new(request):
    if request.method == 'POST':
        data = {
            'producto': request.POST.get('producto'),
            'claveskumaquila': request.POST.get('clavesku_maquila'),
            'presentacion': request.POST.get('presentacion'),
            'noordenproduccion': request.POST.get('noorden_produccion'),
            'numerolote': request.POST.get('numero_lote'),
            'fechacaducidad': request.POST.get('fecha_caducidad'),
            'fechainicioproceso': request.POST.get('fechainicio_proceso'),
            'fechaterminoproceso': request.POST.get('fechatermino_proceso'),
            'rendimientoteorico': request.POST.get('rendimiento_teorico'),
            'rendimientoreal': request.POST.get('rendimiento_real'),
        }

        if not all(data.values()):
            return HttpResponseBadRequest('Faltan datos obligatorios para la orden de producción.')

        orden = OrdenProduccion.objects.create(**data)

        detalles_json = request.POST.get('detalle_orden')
        if detalles_json:
            try:
                detalles = json.loads(detalles_json)
            except json.JSONDecodeError:
                return HttpResponseBadRequest('Error al procesar los detalles de la orden.')
        else:
            return HttpResponseBadRequest('Faltan detalles para la orden de producción.')

        for detalle_data in detalles:
            try:
                cantidad_raw = detalle_data.get('cantidad')
                cantidad = Decimal(cantidad_raw) if cantidad_raw else Decimal('0')

                
                DetalleOrden.objects.create(
                    orden=orden,
                    skump=detalle_data['sku'],
                    material=detalle_data['material'],
                    nolote=detalle_data['lote'],
                    unidad=detalle_data['unidad'],
                    cantidad=cantidad,
                    surtio=detalle_data['surtio'],
                    verifico=detalle_data['verifico']
                )
            except KeyError as e:
                return HttpResponseBadRequest(f'Error en los detalles de la orden: {str(e)}')
        
        print(detalles)  

        usuarios_almacen = RegistroUsuario.objects.filter(user_type='alm')
        for usuario in usuarios_almacen:
            Notificacion.objects.create(
                usuario=usuario,
                mensaje = f'Se ha creado una nueva Orden de Producción <a href="{reverse("marcar_notificacion_leida", args=[orden.id])}">#{orden.id} N° {orden.noordenproduccion}.</a>'
            )

        messages.success(request, 'Orden de Producción creada y notificación enviada.')
        del request.session['detalle_orden']
        request.session.modified = True

        return redirect('ordenproduccionview')

    return render(request, 'contacts/orden_produccion_create.html')

from django.views import generic
from django.shortcuts import get_object_or_404
from .models import FormatoRecepcionMateriaPrima, KardexRecepcionMateriaPrimaAlmacen

class OrdenProduccionView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/orden_produccion_create.html'
    context_object_name = 'ordenes'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        queryset = FormatoRecepcionMateriaPrima.objects.all()

        if q:
            queryset = queryset.filter(materiaprima__icontains=q)

        queryset = queryset.prefetch_related('kardexrecepcionmateriaprimaalmacen_set')
        return queryset

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            data = []
            for orden in context['ordenes']:
                ultimo_kardex = orden.kardexrecepcionmateriaprimaalmacen_set.last()
                cantidad_queda = ultimo_kardex.cantidadqueda if ultimo_kardex else orden.pesoneto

                data.append({
                    'id': orden.id,
                    'materiaprima': orden.materiaprima,
                    'fechaentrada': orden.fechaentrada.strftime('%d/%m/%Y') if orden.fechaentrada else '-',
                    'loteseprisa': orden.loteseprisa or '-',
                    'fechacaducidad': orden.fechacaducidad.strftime('%d/%m/%Y') if orden.fechacaducidad else '-',
                    'pesoneto': orden.pesoneto or '0',
                    'claveproveedor': orden.claveproveedor or '-',
                    'sku': orden.sku or '-',
                    'cantidadqueda': cantidad_queda,
                })
            return JsonResponse({'ordenes': data})
        return super().render_to_response(context, **response_kwargs)

    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)

            context['detalle_orden'] = self.request.session.get('detalle_orden', [])

            return context

from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views import generic
from .models import FormatoRecepcionMateriaPrima, DetalleOrden

from django.shortcuts import get_object_or_404
from .models import OrdenProduccion, DetalleOrden

class OrdenProduccionViewList(generic.ListView):
    model = OrdenProduccion
    paginate_by = 15
    template_name = 'contacts/orden_produccion_create_listview.html'
    context_object_name = 'ordenes'

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        queryset = OrdenProduccion.objects.all()

        if q:
            queryset = queryset.filter(producto__icontains=q)

        queryset = queryset.prefetch_related('detalles')  
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orden_id = self.kwargs.get('pk')  
        orden_seleccionada = get_object_or_404(OrdenProduccion, pk=orden_id)

        detalles_orden = DetalleOrden.objects.filter(orden=orden_seleccionada)

        context['orden_seleccionada'] = orden_seleccionada
        context['detalles_orden'] = detalles_orden

        return context


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import KardexRecepcionMateriaPrimaAlmacen, DetalleOrden, OrdenProduccion

def registrar_salida(request, orden_id, kardex_id):
    orden = OrdenProduccion.objects.get(id=orden_id)
    kardex = KardexRecepcionMateriaPrimaAlmacen.objects.get(id=kardex_id)

    if request.method == "POST":
        cantidad_salida = float(request.POST['cantidad_salida'])

        if cantidad_salida <= kardex.cantidadqueda:
            kardex.cantidadqueda -= cantidad_salida
            kardex.save()

            detalle = DetalleOrden(
                orden=orden,
                skump=kardex.sku,
                material=kardex.materiaprima,
                nolote=kardex.noloteproveedor,
                unidad="kg", 
                cantidad=str(cantidad_salida),  
                surtio=request.user.username,  
                verifico="", 
                observaciones=request.POST.get('observaciones', '') 
            )
            detalle.save()

            return HttpResponse("Salida registrada correctamente")

        else:
            return HttpResponse("La cantidad solicitada es mayor que la cantidad disponible")

    return render(request, "orden_produccion_list_2.html", {'kardex': kardex})


from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import json
from .models import DetalleOrden, OrdenProduccion, KardexRecepcionMateriaPrimaAlmacen

def guardar_detalle_orden(request, orden_id):
    if request.method == "POST":
        try:
            orden = get_object_or_404(OrdenProduccion, id=orden_id)
            
            data = json.loads(request.body)

            for item in data:
                kardex = KardexRecepcionMateriaPrimaAlmacen.objects.filter(sku=item["skump"], noloteproveedor=item["nolote"]).first()

                if kardex and float(item["cantidad"]) <= kardex.cantidadqueda:
                    kardex.cantidadqueda -= float(item["cantidad"])
                    kardex.save()

                    DetalleOrden.objects.create(
                        orden=orden,
                        skump=item["skump"],
                        material=item["material"],
                        nolote=item["nolote"],
                        unidad=item["unidad"],
                        cantidad=float(item["cantidad"]),
                        surtio=item["surtio"],
                        verifico=item["verifico"],
                        observaciones=item["observaciones"]
                    )
                else:
                    return JsonResponse({"success": False, "message": "Cantidad insuficiente en stock"}, status=400)

            return JsonResponse({"success": True, "message": "Datos guardados correctamente"})

        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)}, status=400)

    return JsonResponse({"success": False, "message": "Método no permitido"}, status=405)


from django.views import generic
from django.db.models import Q
from .models import FormatoRecepcionMateriaPrima, OrdenProduccion

from django.views import generic
from django.db.models import Q
from .models import FormatoRecepcionMateriaPrima, OrdenProduccion

from django.db.models import QuerySet
from django.views import generic
from .models import FormatoRecepcionMateriaPrima, OrdenProduccion
from typing import Any

from django.db.models import Q
from django.views import generic
from .models import FormatoRecepcionMateriaPrima, OrdenProduccion
from typing import Any

from django.shortcuts import render, get_object_or_404
from .models import OrdenProduccion
def buscar_ordenproduccion(request):
    orden_produccion = None
    search_query = request.GET.get('search_noorden', '').strip()

    if search_query:
        orden_produccion = OrdenProduccion.objects.filter(noordenproduccion=search_query).first()

    return render(request, 'contacts/orden_produccion_list_2.html', {'OrdenProduccion': orden_produccion})
    
from django.shortcuts import render
from .models import OrdenProduccion, FormatoRecepcionMateriaPrima
from django.db.models import Q

class KardexListViewView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/kardex2.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        queryset = FormatoRecepcionMateriaPrima.objects.all()

        if q:
            queryset = queryset.filter(materiaprima__icontains=q)

        queryset = queryset.prefetch_related('kardexrecepcionmateriaprimaalmacen_set')

        return queryset

class KardexListVView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/kardex2_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        queryset = FormatoRecepcionMateriaPrima.objects.all()

        if q:
            queryset = queryset.filter(materiaprima__icontains=q)

        queryset = queryset.prefetch_related('kardexrecepcionmateriaprimaalmacen_set')

        return queryset


def buscar_kardex(request):
    etiqueta = None
    object_list = [] 

    if 'q' in request.GET:
        query = request.GET['q']
        etiqueta = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=query).first()

        if etiqueta:
            object_list = KardexRecepcionMateriaPrimaAlmacen.objects.filter(formato_recepcion=etiqueta)

    return render(request, 'contacts/kardex.html', {
        'etiqueta': etiqueta,
        'object_list': object_list
    })

class ControlAseguramientoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/control_aseguramiento_calidad.html')
    
from django.http import HttpResponse
from io import BytesIO
from django.template.loader import get_template
from xhtml2pdf import pisa
def export_control_aseguramiento_pdf(request):
    context = {}

    template_path = 'contacts/control_aseguramiento_calidad_pdf.html'
    template = get_template(template_path)

    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ControlAseguramiento.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

def export_control_aseguramiento2_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/control_aseguramiento_calidad_pdf2.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="ControlAseguramiento2.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response
    
class MenuPView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/menu copy 2.html')
    
class MenuPrView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/menuprueba3.html')
    
class FormatoBitacoraProductoTerminadoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_bitacora_producto_terminado.html')
    
def export_bitacora_producto_terminado_pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_ids = data.get('ids', [])

        if not selected_ids:
            return JsonResponse({"error": "No IDs provided"}, status=400)

        objects = FormatoBitacoraProductoTerminado.objects.filter(pk__in=selected_ids)

        template_path = 'contacts/formato_bitacora_producto_terminado_pdf.html'
        context = {'FormatoBitacoraProductoTerminadox': objects}

        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="FormatoBitacoraProductoTerminado.pdf"'

        result = BytesIO()
        pisa_status = pisa.CreatePDF(
            BytesIO(html.encode("UTF-8")),
            dest=result,
            encoding='UTF-8'
        )

        if pisa_status.err:
            return HttpResponse('Error generando el PDF', status=500)

        response.write(result.getvalue())
        return response

    return JsonResponse({"error": "Invalid request"}, status=400)

class FormatoBitacoraProductoTerminadoView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/formato_bitacora_producto_terminado.html')
    
from django.views.generic import ListView
    
class FormatoBitacoraProductoTerminadoListView(ListView):
    model = FormatoBitacoraProductoTerminado
    template_name = 'contacts/formato_bitacora_producto_terminado.html'
    context_object_name = "object_list"
    paginate_by = 15  

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(producto__icontains=query) |
                Q(lote__icontains=query) |
                Q(sku__icontains=query)
            )
        return queryset

from django.http import JsonResponse
from django.template.loader import render_to_string
from .models import FormatoBitacoraProductoTerminado
from django.db.models import Q

def formato_bitacora_producto_terminado_list(request):
    query = request.GET.get("q", "")
    page = int(request.GET.get("page", 1))
    items_per_page = 15
    start = (page - 1) * items_per_page
    end = start + items_per_page

    queryset = FormatoBitacoraProductoTerminado.objects.filter(
        Q(producto__icontains=query) |
        Q(clave_proveedor__icontains=query)
    )[start:end]
    
    table_html = render_to_string("partials/formato_recepcion_table_body.html", {"object_list": queryset})
    
    return JsonResponse({
        "table_body": table_html,
        "has_next": len(queryset) == items_per_page,  
        "has_previous": page > 1
    })

class FormatoBitacoraProductoTerminadoCreateView(generic.CreateView):
    model = FormatoBitacoraProductoTerminado
    fields = ('fechaentrada','producto','lote','sku','presentacion','contenedores','cliente','noanalisis','fechacaducidad','recibe','contenedores',)

    success_url = reverse_lazy('formato_bitacora_producto_terminado')
    template_name='contacts/formato_bitacora_producto_terminado_form.html'

class FormatoBitacoraProductoTerminadoUpdateView(generic.UpdateView):
    model = FormatoBitacoraProductoTerminado
    fields = ('fechaentrada','producto','lote','sku','presentacion','contenedores','cliente','noanalisis','fechacaducidad','recibe','contenedores',)
    success_url = reverse_lazy('formato_bitacora_producto_terminado')
    template_name='contacts/formato_bitacora_producto_terminado_form.html'

class FormatoBitacoraProductoTerminadoDeleteView(generic.DeleteView):
    model = FormatoBitacoraProductoTerminado
    success_url = reverse_lazy('formato_bitacora_producto_terminado')
    template_name='contacts/formato_bitacora_producto_terminado_confirm_delete.html'


class FormatoBitacoraProductoTerminadoListViewView(generic.ListView):
    model = FormatoBitacoraProductoTerminado
    paginate_by = 15
    template_name = 'contacts/formato_bitacora_producto_terminado_view.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return FormatoBitacoraProductoTerminado.objects.filter(material__icontains=q)
        return super().get_queryset()

from django.shortcuts import render
from .models import KardexRecepcionMateriaPrimaAlmacen

from decimal import Decimal
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import FormatoRecepcionMateriaPrima, KardexRecepcionMateriaPrimaAlmacen

from django.shortcuts import redirect

class GuardarKardexView(View):
    def post(self, request, *args, **kwargs):
        formato_id = request.POST.get('id')

        if not formato_id:
            return render(request, 'contacts/kardex.html', {'error': 'ID de formato no encontrado.'})

        formato_recepcion = get_object_or_404(FormatoRecepcionMateriaPrima, id=formato_id)

        fechasalida = request.POST.get('fecha_salida')
        if not fechasalida:
            return render(request, 'contacts/kardex.html', {'error': 'La fecha de salida es obligatoria.'})

        try:
            cantidad_sale = Decimal(request.POST.get('cantidad_sale', "0"))
        except:
            return render(request, 'contacts/kardex.html', {'error': 'Cantidad de salida no válida.'})

        ultima_salida = KardexRecepcionMateriaPrimaAlmacen.objects.filter(
            formato_recepcion=formato_recepcion
        ).order_by('-id').first()

        cantidad_queda_anterior = (
            ultima_salida.cantidadqueda if ultima_salida else formato_recepcion.cantidadneto
        )

        cantidad_queda_anterior = Decimal(str(cantidad_queda_anterior)) if cantidad_queda_anterior is not None else Decimal("0")

        cantidad_queda_actual = cantidad_queda_anterior - cantidad_sale

        if cantidad_queda_actual < 0:
            return render(request, 'contacts/kardex.html', {'error': 'No puedes sacar más de lo que hay disponible.'})

        try:
            kardex = KardexRecepcionMateriaPrimaAlmacen(
                materiaprima=formato_recepcion.materiaprima,
                fechacaducidad=formato_recepcion.fechacaducidad,
                noloteseprisa=formato_recepcion.loteseprisa,
                fechaentrada=formato_recepcion.fechaentrada,
                cantidadneto=formato_recepcion.pesoneto,
                codigoproveedorcliente=formato_recepcion.claveproveedor,
                sku=formato_recepcion.sku,
                fechasalida=fechasalida,
                clienteusointerno=request.POST.get('cliente_usointerno', ''),
                noloteproveedor=formato_recepcion.noloteproveedor,
                cantidadsale=cantidad_sale,
                cantidadqueda=cantidad_queda_actual,
                realizo=request.POST.get('realizo', ''),
                observaciones=request.POST.get('observaciones', ''),
                formato_recepcion=formato_recepcion
            )
            kardex.save()

            return redirect(f'/kardexlist/?id={formato_id}')

        except Exception as e:
            return render(request, 'contacts/kardex.html', {'error': f'No se pudo guardar el kardex: {e}'})

from django.shortcuts import get_object_or_404, redirect
from decimal import Decimal

from django.shortcuts import redirect
from decimal import Decimal

class GuardarKardexProdView(View):
    def post(self, request, *args, **kwargs):
        formato_id = request.POST.get('id')
        if not formato_id:
            return render(request, 'contacts/kardexprod.html', {'error': 'ID de formato no encontrado.'})

        formato_recepcion = get_object_or_404(FormatoRecepcionMateriaPrima, id=formato_id)

        fechasalida = request.POST.get('fecha_salida')
        if not fechasalida:
            return render(request, 'contacts/kardexprod.html', {'error': 'La fecha de salida es obligatoria.'})

        try:
            cantidad_sale = Decimal(request.POST.get('cantidad_sale', "0"))
        except:
            return render(request, 'contacts/kardexprod.html', {'error': 'Cantidad de salida no válida.'})

        ultima_salida = KardexRecepcionMateriaPrimaAlmacen.objects.filter(
            formato_recepcion=formato_recepcion
        ).order_by('-id').first()

        cantidad_queda_anterior = (
            ultima_salida.cantidadqueda if ultima_salida else formato_recepcion.pesoneto
        )
        cantidad_queda_actual = Decimal(str(cantidad_queda_anterior)) - cantidad_sale

        if cantidad_queda_actual < 0:
            return render(request, 'contacts/kardexprod.html', {'error': 'No puedes sacar más de lo que hay disponible.'})

        try:
            kardex = KardexRecepcionMateriaPrimaAlmacen.objects.create(
                materiaprima=formato_recepcion.materiaprima,
                fechacaducidad=formato_recepcion.fechacaducidad,
                noloteseprisa=formato_recepcion.loteseprisa,
                fechaentrada=formato_recepcion.fechaentrada,
                cantidadneto=formato_recepcion.pesoneto,
                codigoproveedorcliente=formato_recepcion.claveproveedor,
                sku=formato_recepcion.sku,
                fechasalida=fechasalida,
                clienteusointerno=request.POST.get('cliente_usointerno', ''),
                noloteproveedor=request.POST.get('lote_proveedor', ''),
                cantidadsale=cantidad_sale,
                cantidadqueda=cantidad_queda_actual,
                realizo=request.POST.get('realizo', ''),
                observaciones=request.POST.get('observaciones', ''),
                formato_recepcion=formato_recepcion
            )

            if 'detalle_orden' not in request.session:
                request.session['detalle_orden'] = []

            request.session['detalle_orden'].append({
                'sku': formato_recepcion.sku,
                'material': formato_recepcion.materiaprima,
                'lote': formato_recepcion.loteseprisa,
                'unidad': 'kg', 
                'cantidad': str(cantidad_sale),  
                'surtio': request.POST.get('realizo', ''),
                'verifico': '',
            })

            request.session.modified = True 

            return redirect('ordenproduccionview')

        except Exception as e:
            return render(request, 'contacts/kardexprod.html', {'error': f'No se pudo guardar el kardex: {e}'})


from django.contrib.auth.models import User 
from .models import Notificacion, KardexRecepcionMateriaPrimaAlmacen

class KardexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/kardex.html')

from django.shortcuts import render, get_object_or_404
from .models import FormatoRecepcionMateriaPrima

def kardex_listlist(request):
    id = request.GET.get('id')

    if id:
        etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, pk=id)

        pesoneto = etiqueta.pesoneto or 0
        nocontenedores = etiqueta.nocontenedores or 0
        cantidad_neta = pesoneto * nocontenedores
        
        salidas = etiqueta.kardexrecepcionmateriaprimaalmacen_set.all()
        
        return render(request, 'contacts/kardex.html', {'etiqueta': etiqueta, 'salidas': salidas, 'cantidad_neta': cantidad_neta})
    else:
        return render(request, 'contacts/kardex.html', {'error': 'ID no proporcionado'})
    
def kardex_prodlist(request):
    id = request.GET.get('id')

    if id:
        etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, pk=id)
        
        salidas = etiqueta.kardexrecepcionmateriaprimaalmacen_set.all()
        
        return render(request, 'contacts/kardexprod.html', {'etiqueta': etiqueta, 'salidas': salidas})
    else:
        return render(request, 'contacts/kardexprod.html', {'error': 'ID no proporcionado'})

class KardexListView(generic.ListView):
    model = KardexRecepcionMateriaPrimaAlmacen
    paginate_by = 15
    template_name = 'contacts/kardex.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        if q:
            return KardexRecepcionMateriaPrimaAlmacen.objects.filter(materiaprima__icontains=q)
        return super().get_queryset()
    
class KardexListViewView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/kardex2.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(materiaprima__icontains=query) |
                Q(loteseprisa__icontains=query) |
                Q(sku__icontains=query)
            )
        return queryset

class KardexListVView(generic.ListView):
    model = FormatoRecepcionMateriaPrima
    paginate_by = 15
    template_name = 'contacts/kardex2_list.html'

    def get_queryset(self) -> QuerySet[Any]:
        q = self.request.GET.get('q')

        queryset = FormatoRecepcionMateriaPrima.objects.all()

        if q:
            queryset = queryset.filter(materiaprima__icontains=q)

        queryset = queryset.prefetch_related('kardexrecepcionmateriaprimaalmacen_set')

        return queryset


def buscar_kardex(request):
    etiqueta = None
    object_list = [] 

    if 'q' in request.GET:
        query = request.GET['q']
        etiqueta = FormatoRecepcionMateriaPrima.objects.filter(materiaprima__icontains=query).first()

        if etiqueta:
            object_list = KardexRecepcionMateriaPrimaAlmacen.objects.filter(formato_recepcion=etiqueta)

    return render(request, 'contacts/kardex.html', {
        'etiqueta': etiqueta,
        'object_list': object_list
    })

class KardexCreateView(generic.CreateView):
    model = KardexRecepcionMateriaPrimaAlmacen
    fields = (
        'materiaprima', 'fechacaducidad', 'noloteseprisa', 'fechaentrada', 
        'cantidadneto', 'codigoproveedorcliente', 'sku', 
        'fechasalida', 'clienteusointerno', 'noloteproveedor', 
        'cantidadsale', 'cantidadqueda', 'realizo', 'observaciones'
    )
    success_url = reverse_lazy('kardex_list')
    template_name = 'contacts/kardex.html'
    

class KardexUpdateView(generic.UpdateView):
    model = KardexRecepcionMateriaPrimaAlmacen
    fields = ('fechasalida','clienteusointerno','noloteproveedor','cantidadsale','cantidadqueda','realizo','observaciones')
    success_url = reverse_lazy('kardex_list')
    template_name='contacts/kardex_form.html'

class KardexDeleteView(generic.DeleteView):
    model = KardexRecepcionMateriaPrimaAlmacen
    success_url = reverse_lazy('kardex_list')
    template_name='contacts/kardex_confirm_delete.html'


import json
from io import BytesIO
from django.http import HttpResponse, JsonResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import FormatoRecepcionMateriaPrima, KardexRecepcionMateriaPrimaAlmacen

def export_formato_kardex_pdf2(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        selected_ids = data.get('ids', [])

        if not selected_ids:
            return JsonResponse({"error": "No IDs provided"}, status=400)

        formatos = FormatoRecepcionMateriaPrima.objects.filter(pk__in=selected_ids)
        kardexs = KardexRecepcionMateriaPrimaAlmacen.objects.filter(pk__in=selected_ids)

        template_path = 'contacts/kardex_pdf2.html'
        context = {
            'FormatoRecepcionMateriaPrimax': formatos,
            'KardexRecepcionMateriaPrimaAlmacens': kardexs
        }

        template = get_template(template_path)
        html = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="KARDEX.pdf"'

        result = BytesIO()
        pisa_status = pisa.CreatePDF(
            BytesIO(html.encode("UTF-8")),
            dest=result,
            encoding='UTF-8'
        )

        if pisa_status.err:
            return HttpResponse('Error generando el PDF', status=500)

        response.write(result.getvalue())
        return response

    return JsonResponse({"error": "Invalid request"}, status=400)


from django.shortcuts import render
from .models import OrdenProduccion

from django.shortcuts import render
from .models import OrdenProduccion, Muestra, Tabla

def buscar_orden_produccion(request):
    orden_produccion = None
    tabla1_muestras = []  
    tabla2_muestras = []  
    search_query = request.GET.get('search_noorden', '')

    if search_query:
        try:
            orden_produccion = OrdenProduccion.objects.get(noordenproduccion=search_query)
            
            muestras1 = Muestra.objects.filter(orden_produccion=orden_produccion, columna__gte=1, columna__lte=13).order_by('fila', 'columna')

            muestras2 = Muestra.objects.filter(orden_produccion=orden_produccion, columna__gte=14, columna__lte=26).order_by('fila', 'columna')

            filas1 = {}
            for muestra in muestras1:
                if muestra.fila not in filas1:
                    filas1[muestra.fila] = [None] * 13  

                if 1 <= muestra.columna <= 13:
                    filas1[muestra.fila][muestra.columna - 1] = muestra.valor 

            tabla1_muestras = [{'fila': fila, 'valores': valores} for fila, valores in filas1.items()]

            for fila in range(1, 11):
                if fila not in filas1:
                    filas1[fila] = [None] * 13  

            tabla1_muestras = [{'fila': fila, 'valores': filas1.get(fila, [None] * 13)} for fila in range(1, 11)]

            filas2 = {}
            for muestra in muestras2:
                if muestra.fila not in filas2:
                    filas2[muestra.fila] = [None] * 13  
                
                if 14 <= muestra.columna <= 26:
                    filas2[muestra.fila][muestra.columna - 14] = muestra.valor  

            tabla2_muestras = [{'fila': fila, 'valores': valores} for fila, valores in filas2.items()]

            # Asegurarse de que todas las filas 1-10 estén presentes en tabla2
            for fila in range(1, 11):
                if fila not in filas2:
                    filas2[fila] = [None] * 13  # Filas vacías

            tabla2_muestras = [{'fila': fila, 'valores': filas2.get(fila, [None] * 13)} for fila in range(1, 11)]

        except OrdenProduccion.DoesNotExist:
            orden_produccion = None

    return render(request, 'contacts/control_aseguramiento_calidad.html', {
        'OrdenProduccion': orden_produccion,
        'tabla1_muestras': tabla1_muestras,
        'tabla2_muestras': tabla2_muestras  
    })

def buscar_orden_produccion_view(request):
    orden_produccion = None
    tabla1_muestras = []  
    tabla2_muestras = []  
    search_query = request.GET.get('search_noorden', '')

    if search_query:
        try:
            orden_produccion = OrdenProduccion.objects.get(noordenproduccion=search_query)
            
            muestras1 = Muestra.objects.filter(orden_produccion=orden_produccion, columna__gte=1, columna__lte=13).order_by('fila', 'columna')

            muestras2 = Muestra.objects.filter(orden_produccion=orden_produccion, columna__gte=14, columna__lte=26).order_by('fila', 'columna')

            filas1 = {}
            for muestra in muestras1:
                if muestra.fila not in filas1:
                    filas1[muestra.fila] = [None] * 13  
                
                if 1 <= muestra.columna <= 13:
                    filas1[muestra.fila][muestra.columna - 1] = muestra.valor  

            tabla1_muestras = [{'fila': fila, 'valores': valores} for fila, valores in filas1.items()]

            for fila in range(1, 11):
                if fila not in filas1:
                    filas1[fila] = [None] * 13  

            tabla1_muestras = [{'fila': fila, 'valores': filas1.get(fila, [None] * 13)} for fila in range(1, 11)]

            filas2 = {}
            for muestra in muestras2:
                if muestra.fila not in filas2:
                    filas2[muestra.fila] = [None] * 13  
                
                if 14 <= muestra.columna <= 26:
                    filas2[muestra.fila][muestra.columna - 14] = muestra.valor  
            tabla2_muestras = [{'fila': fila, 'valores': valores} for fila, valores in filas2.items()]

            for fila in range(1, 11):
                if fila not in filas2:
                    filas2[fila] = [None] * 13  

            tabla2_muestras = [{'fila': fila, 'valores': filas2.get(fila, [None] * 13)} for fila in range(1, 11)]

        except OrdenProduccion.DoesNotExist:
            orden_produccion = None

    return render(request, 'contacts/control_aseguramiento_calidad_view.html', {
        'OrdenProduccion': orden_produccion,
        'tabla1_muestras': tabla1_muestras,
        'tabla2_muestras': tabla2_muestras  
    })


#no lo ocupo
def buscar_orden(request):
    search_noorden = request.GET.get('search_noorden')
    if not search_noorden:
        messages.error(request, "Número de orden no recibido")
        return redirect('ruta_donde_redirigir')
    
    orden = OrdenProduccion.objects.filter(numero=search_noorden).first()
    if orden:
        pass
    else:
        messages.error(request, "No se encontró la orden")
    return render(request, 'contacts/control_aseguramiento_calidad.html', {'orden': orden})


from django.http import JsonResponse
import json
from .models import Muestra, Tabla


from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import OrdenProduccion, Muestra, Tabla


from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .models import OrdenProduccion, Muestra, Tabla


@csrf_exempt
def guardar_muestras(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            numero_orden = data.get("numero_orden")

            if not numero_orden:
                return JsonResponse({"error": "Número de orden no recibido o vacío"}, status=400)

            try:
                orden_produccion = OrdenProduccion.objects.get(noordenproduccion=numero_orden)
            except OrdenProduccion.DoesNotExist:
                return JsonResponse({"error": "Orden de producción no encontrada"}, status=404)

            tabla1 = data.get("tabla1", [])
            tabla2 = data.get("tabla2", [])

            Muestra.objects.filter(orden_produccion=orden_produccion).delete()

            filas_existentes = set(item["fila"] for item in tabla1 + tabla2)

            for fila in range(1, 11):
                if fila not in filas_existentes:
                    tabla1.append({"fila": fila, "columna": 1, "valor": None})  
                    tabla2.append({"fila": fila, "columna": 14, "valor": None})  

            muestras = [
                Muestra(
                    orden_produccion=orden_produccion,
                    noordenproduccion=orden_produccion.noordenproduccion,
                    fila=item["fila"],
                    columna=item["columna"],
                    valor=item["valor"]
                )
                for item in tabla1 + tabla2 
            ]

            if muestras:  
                Muestra.objects.bulk_create(muestras)

            tabla = Tabla.objects.create(orden_produccion=orden_produccion)
            tabla.tabla1_muestras.set(
                Muestra.objects.filter(orden_produccion=orden_produccion, columna__lte=13)
            )
            tabla.tabla2_muestras.set(
                Muestra.objects.filter(orden_produccion=orden_produccion, columna__gt=13)
            )

            return JsonResponse({"mensaje": "Datos guardados correctamente"})

        except json.JSONDecodeError:
            return JsonResponse({"error": "Error al procesar los datos JSON"}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)




class BitacoraProductoterminadoListViewView(generic.ListView):
    model = FormatoBitacoraProductoTerminado
    paginate_by = 15
    template_name = 'contacts/formato_bitacora_producto_terminado_2.html'
    
    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(producto__icontains=query) |
                Q(lote__icontains=query) |
                Q(sku__icontains=query)
            )
        return queryset
    
def obtener_muestras(request, numero_orden):
    orden_produccion = None
    search_query = request.GET.get('search_noorden', '')

    if search_query:
        try:
            orden_produccion = OrdenProduccion.objects.get(noordenproduccion=search_query)
        except OrdenProduccion.DoesNotExist:
            orden_produccion = None

        return render(request, 'contacts/control_aseguramiento_calidad.html', {'OrdenProduccion': orden_produccion})
    try:
        orden = OrdenProduccion.objects.get(noordenproduccion=numero_orden)
        muestras = Muestra.objects.filter(orden_produccion=orden)

        datos_muestras = {
            "tabla1": [],
            "tabla2": []
        }

        for muestra in muestras:
            if muestra.columna <= 13:
                datos_muestras["tabla1"].append({
                    "fila": muestra.fila,
                    "columna": muestra.columna,
                    "valor": muestra.valor
                })
            else:
                datos_muestras["tabla2"].append({
                    "fila": muestra.fila,
                    "columna": muestra.columna,
                    "valor": muestra.valor
                })

        return JsonResponse(datos_muestras)

    except OrdenProduccion.DoesNotExist:
        return JsonResponse({"error": "Orden de producción no encontrada"}, status=404)


def control_aseguramiento_calidad_list(request):
    return render(request, 'contacts/control_aseguramiento_calidad_2.html')

class ControlaseguramientocalidadListView(ListView):
    model = OrdenProduccion
    template_name = 'contacts/control_aseguramiento_calidad_2.html'
    context_object_name = "object_list"
    paginate_by = 15  

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(producto__icontains=query) |
                Q(claveskumaquila__icontains=query) |
                Q(noordenproduccion__icontains=query)
            )
        return queryset
    
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import OrdenProduccion, DetalleOrden  

def obtener_orden_produccion(request, no_orden):
    try:
        orden = get_object_or_404(OrdenProduccion, no_orden=no_orden)

        detalles = DetalleOrden.objects.filter(orden=orden).values()

        return JsonResponse({
            'success': True,
            'orden': {
                'no_orden': orden.no_orden,
                'fecha': orden.fecha.strftime('%Y-%m-%d'),
                'cliente': orden.cliente,
                'producto': orden.producto,
                'cantidad': orden.cantidad,
                'estado': orden.estado,
            },
            'detalles': list(detalles)
        })
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})
    
class ControlaseguramientocalidadListViewV(ListView):
    model = OrdenProduccion
    template_name = 'contacts/control_aseguramiento_calidad_2_view.html'
    context_object_name = "object_list"
    paginate_by = 15  

    def get_queryset(self):
        query = self.request.GET.get("q")
        queryset = super().get_queryset()
        if query:
            queryset = queryset.filter(
                Q(producto__icontains=query) |
                Q(claveskumaquila__icontains=query) |
                Q(noordenproduccion__icontains=query)
            )
        return queryset

from django.shortcuts import render
from .models import Notificacion, RegistroUsuario

def ver_notificaciones(request):
    if request.user.user_type == 'alm':
        notificaciones = Notificacion.objects.filter(usuario__user_type='alm').order_by('-fecha_creacion')
    else:
        notificaciones = []  

    return render(request, 'contacts/notificaciones.html', {'notificaciones': notificaciones})

import re

@login_required
def marcar_notificacion_leida(request, notificacion_id):
    try:
        notificacion = Notificacion.objects.get(id=notificacion_id, usuario=request.user)
        notificacion.leida = True
        notificacion.save()

        # Extraer ID de orden desde el mensaje
        import re
        match = re.search(r'#(\d+)', notificacion.mensaje)
        if match:
            orden_id = match.group(1)
            return redirect('ordenproduccionviewlist', pk=orden_id)
    except Notificacion.DoesNotExist:
        messages.error(request, 'No se pudo redirigir')

    return redirect('ver_notificaciones')

@login_required
def redirigir_a_orden(request, notificacion_id):
    try:
        notificacion = Notificacion.objects.get(id=notificacion_id, usuario=request.user)

        import re
        match = re.search(r'#(\d+)', notificacion.mensaje)
        if match:
            orden_id = match.group(1)
            return redirect('ordenproduccionviewlist', pk=orden_id)
        else:
            messages.error(request, 'No se encontró un ID de orden en la notificación.')
    except Notificacion.DoesNotExist:
        messages.error(request, 'Notificación no encontrada.')

    return redirect('ver_notificaciones')

from django.views import View
from django.http import JsonResponse
from decimal import Decimal
from .models import KardexRecepcionMateriaPrimaAlmacen

class EditarDetalleOrdenView(View):
    def post(self, request):
        index = int(request.POST.get('index'))
        nueva_cantidad = Decimal(request.POST.get('cantidad'))

        detalle_orden = request.session.get('detalle_orden', [])

        if index >= len(detalle_orden):
            return JsonResponse({'error': 'Índice no válido'}, status=400)

        producto = detalle_orden[index]
        sku = producto['sku']
        lote = producto['lote']
        cantidad_original = Decimal(producto['cantidad'])

        kardex = KardexRecepcionMateriaPrimaAlmacen.objects.filter(
            sku=sku, noloteseprisa=lote
        ).order_by('-id').first()

        if not kardex:
            return JsonResponse({'error': 'Registro de Kardex no encontrado'}, status=404)

        cantidad_disponible = kardex.cantidadqueda + cantidad_original

        if nueva_cantidad > cantidad_disponible:
            return JsonResponse({'error': 'Cantidad excede lo disponible en stock'}, status=400)

        kardex.cantidadsale = nueva_cantidad
        kardex.cantidadqueda = cantidad_disponible - nueva_cantidad
        kardex.save()

        producto['cantidad'] = str(nueva_cantidad)
        request.session['detalle_orden'][index] = producto
        request.session.modified = True

        return JsonResponse({'success': True})


class EliminarDetalleOrdenView(View):
    def post(self, request):
        index = int(request.POST.get('index'))

        detalle_orden = request.session.get('detalle_orden', [])

        if index >= len(detalle_orden):
            return JsonResponse({'error': 'Índice no válido'}, status=400)

        producto = detalle_orden.pop(index)
        sku = producto['sku']
        lote = producto['lote']
        cantidad = Decimal(producto['cantidad'])

        kardex = KardexRecepcionMateriaPrimaAlmacen.objects.filter(
            sku=sku, noloteseprisa=lote
        ).order_by('-id').first()

        if kardex:
            kardex.cantidadqueda += cantidad
            kardex.save()

        request.session['detalle_orden'] = detalle_orden
        request.session.modified = True

        return JsonResponse({'success': True})



import io
import os
import json
from django.http import FileResponse, HttpResponse
from django.conf import settings
from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def descargar_control(request):
    if request.method == "POST":
        try:
            try:
                data = json.loads(request.body)
                muestras = data.get('muestras', [])
            except json.JSONDecodeError:
                return HttpResponse("Error al decodificar JSON", status=400)
            
            pdf_path = os.path.join(settings.BASE_DIR, 'contacts', 'templates', 'contacts', 'ControlAseguramiento.pdf')
            
            if not os.path.exists(pdf_path):
                return HttpResponse(f"El archivo PDF no fue encontrado en: {pdf_path}", status=404)
            
            reader = PdfReader(pdf_path)
            writer = PdfWriter()
            
            packet = io.BytesIO()
            can = canvas.Canvas(packet, pagesize=letter)
            
            coordenadas_muestras_1 = {
                0: [200, 379, 200, 329],  
                1: [248, 379, 248, 329],  
                2: [292, 379, 292, 329],  
                3: [337, 379, 337, 329],  
                4: [385, 379, 385, 329],  
                5: [432, 379, 432, 329],  
                6: [481, 379, 481, 329],  
                7: [530, 379, 530, 329],  
                8: [578, 379, 578, 329],  
                9: [623, 379, 623, 329],  
                10: [670, 379, 670, 329], 
                11: [695, 379, 710, 329], 
                12: [800, 379, 800, 329]  
            }
            
            coordenadas_muestras_2 = {
                0: [200, 221, 200, 221],  
                1: [248, 221, 248, 221],  
                2: [292, 221, 292, 221],  
                3: [337, 221, 337, 221],  
                4: [385, 221, 385, 221],  
                5: [432, 221, 432, 221],  
                6: [481, 221, 481, 221],  
                7: [530, 221, 530, 221],  
                8: [578, 221, 578, 221],  
                9: [623, 221, 623, 221],  
                10: [650, 221, 650, 221], 
                11: [695, 221, 695, 221], 
                12: [800, 221, 800, 221]  
            }

            
            filas_tabla1_y = [379, 369, 359, 349, 339]  
            filas_tabla2_y = [329, 319, 309, 299, 289]  
            
            filas_tabla3_y = [221, 211, 201, 191, 181]  
            filas_tabla4_y = [171, 161, 151, 141, 131]  
            
            promedio_tabla1_y = 329 - 10  
            promedio_tabla2_y = 279       
            promedio_tabla3_y = 229 - 10  
            promedio_tabla4_y = 123       
            
            for col_idx, muestra in enumerate(muestras[:13]):
                if col_idx >= len(coordenadas_muestras_1):
                    break
                    
                tabla1_x = coordenadas_muestras_1[col_idx][0]
                tabla1_y_base = coordenadas_muestras_1[col_idx][1]
                tabla2_x = coordenadas_muestras_1[col_idx][2]
                tabla2_y_base = coordenadas_muestras_1[col_idx][3]
                
                for row_idx in range(0, 5):
                    if row_idx < len(muestra.get('valores', [])):
                        valor = muestra.get('valores', [])[row_idx]
                        if valor:
                            row_y = filas_tabla1_y[row_idx]
                            can.drawString(tabla1_x - 15, row_y - 5, str(valor))
                
                for row_idx in range(5, 10):
                    if row_idx < len(muestra.get('valores', [])):
                        valor = muestra.get('valores', [])[row_idx]
                        if valor:
                            adjusted_row_idx = row_idx - 5
                            row_y = filas_tabla2_y[adjusted_row_idx]
                            can.drawString(tabla2_x - 15, row_y - 5, str(valor))
                
                if 'promedio' in muestra and muestra['promedio']:
                    can.drawString(tabla2_x - 15, promedio_tabla2_y - 5, str(muestra['promedio']))
            
            for col_idx, muestra in enumerate(muestras[13:26]):
                if col_idx >= len(coordenadas_muestras_2):
                    break
                    
                tabla3_x = coordenadas_muestras_2[col_idx][0]
                tabla3_y_base = coordenadas_muestras_2[col_idx][1]
                tabla4_x = coordenadas_muestras_2[col_idx][2]
                tabla4_y_base = coordenadas_muestras_2[col_idx][3]
                
                for row_idx in range(0, 5):
                    if row_idx < len(muestra.get('valores', [])):
                        valor = muestra.get('valores', [])[row_idx]
                        if valor:
                            row_y = filas_tabla3_y[row_idx]
                            can.drawString(tabla3_x - 15, row_y - 5, str(valor))
                
                for row_idx in range(5, 10):
                    if row_idx < len(muestra.get('valores', [])):
                        valor = muestra.get('valores', [])[row_idx]
                        if valor:
                            adjusted_row_idx = row_idx - 5
                            row_y = filas_tabla4_y[adjusted_row_idx]
                            can.drawString(tabla4_x - 15, row_y - 5, str(valor))
                
                if 'promedio' in muestra and muestra['promedio']:
                    can.drawString(tabla4_x - 15, promedio_tabla4_y - 5, str(muestra['promedio']))
            
            can.save()
            packet.seek(0)
            
            overlay = PdfReader(packet)
            
            for i in range(len(reader.pages)):
                page = reader.pages[i]
                if i == 0:  
                    page.merge_page(overlay.pages[0])
                writer.add_page(page)
            
            output_pdf_path = os.path.join(settings.BASE_DIR, 'contacts', 'ControlAseguramiento_modificado.pdf')
            with open(output_pdf_path, "wb") as output_pdf:
                writer.write(output_pdf)
            
            return FileResponse(open(output_pdf_path, "rb"), as_attachment=True, filename="ControlAseguramiento_modificado.pdf")
        
        except Exception as e:
            return HttpResponse(f"Error al procesar el PDF: {str(e)}", status=500)
    
    return HttpResponse("Método no permitido", status=405)