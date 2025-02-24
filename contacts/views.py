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


# Create your views here.
def home(request):
    return render(request, 'contacts/home.html')

# Create your views here.
def menu_principal(request):
    return render(request, 'contacts/menu_principal.html')

# def RegistroUsuarios(request):
#     if request.method == 'POST':
#         form = RegistroUsuarioCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Iniciar sesión automáticamente después del registro
#             return redirect(assign_dashboard(user))  # Redirigir según su tipo de usuario
#     else:
#         form = RegistroUsuarioCreationForm()
#     return render(request, 'contacts/registro_usuarios.html', {'form': form})

# def assign_dashboard(user):
#     """ Asigna la vista del dashboard según el tipo de usuario """
#     dashboard_urls = {
#         'admin': 'menu_admin',
#         'alm': 'menu_almacen',
#         'prod': 'menu_produccion',
#         'cal': 'menu_calidad',
#         'entrada': 'menu_entrada'
#     }
#     return dashboard_urls.get(user.user_type, 'menu_principal')  # Redirige al home si no hay coincidencia

def register(request):
    if request.method == 'POST':
        form = RegistroUsuarioCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Iniciar sesión automáticamente después del registro
            return redirect(assign_dashboard(user))  # Redirigir según su tipo de usuario
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
    return dashboard_urls.get(user.user_type, 'home')  # Redirige al home si no hay coincidencia

from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

class LoginView(LoginView):
    template_name = 'contacts/login.html'

    def form_valid(self, form):
        """ Redirige al menú según el tipo de usuario autenticado """
        usuario = form.get_user()
        login(self.request, usuario)  # Autentica al usuario correctamente

        # 🔍 Verifica en la consola si el usuario se autentica y qué tipo de usuario tiene
        print(f"Usuario autenticado: {usuario.username} - Tipo: {usuario.user_type}")  

        # Diccionario de rutas de redirección según el tipo de usuario
        dashboard_urls = {
            'admin': 'menu_admin',
            'alm': 'menu_almacen',
            'prod': 'menu_produccion',
            'cal': 'menu_calidad',
            'entrada': 'menu_entrada'
        }

        # Obtiene la URL de redirección según el tipo de usuario
        redirect_url = dashboard_urls.get(usuario.user_type, 'home')

        return redirect(redirect_url)

from django.views.generic import ListView

# class RegistroUsuariosListView(ListView):
class UserListView(ListView):
    model = RegistroUsuario
    template_name = 'contacts/registro_usuarios_list.html'  # Crea este template
    context_object_name = 'usuarios'


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import RegistroUsuario
from .forms import RegistroUsuarioCreationForm  # Crea este formulario

# class RegistroUsuariosEditView(UpdateView):
class UserEditView(UpdateView):
    model = RegistroUsuario
    form_class = RegistroUsuarioCreationForm
    template_name = 'contacts/registro_usuarios_edit.html'
    success_url = reverse_lazy('registro_usuarios_list')  # Redirige a la lista después de editar


from django.views.generic import DeleteView

# class RegistroUsuariosDeleteView(DeleteView):
class UserDeleteView(DeleteView):
    model = RegistroUsuario
    template_name = 'contacts/registro_usuarios_confirm_delete.html'
    success_url = reverse_lazy('registro_usuarios_list')

@login_required
def menu_admin(request):
    # Agrega el contenido del dashboard del administrador
    return render(request, 'contacts/menu_admin.html')

@login_required
def menu_entrada(request):
    # Agrega el contenido del dashboard del administrador
    return render(request, 'contacts/menu_entrada.html')

@login_required
def menu_almacen(request):
    # Agrega el contenido del dashboard del administrador
    return render(request, 'contacts/menu_almacen.html')

@login_required
def menu_produccion(request):
    # Agrega el contenido del dashboard del administrador
    return render(request, 'contacts/menu_produccion.html')

@login_required
def menu_almacen(request):
    # Agrega el contenido del dashboard del administrador
    return render(request, 'contacts/menu_almacen.html')

@login_required
def menu_calidad(request):
    # Agrega el contenido del dashboard del administrador
    return render(request, 'contacts/menu_calidad.html')
# # USUARIOS
# class RegistroUsuarioListView(generic.ListView):
#     model = RegistroUsuario
#     paginate_by = 15
#     template_name = 'contacts/registro_usuario.html'
    

#     def get_queryset(self) -> QuerySet[Any]:
#         q = self.request.GET.get('q')

#         if q:
#             return RegistroUsuario.objects.filter(name__icontains=q)

#         return super().get_queryset() 

# class RegistroUsuarioCreateView(generic.CreateView): 
#     model = RegistroUsuario 
#     fields = ('nombre', 'apellidopaterno', 'apellidomaterno', 'tipousuario', 'correo','contraseña', 'confirmacioncontraseña')
#     success_url = reverse_lazy('registrousuario_list')
#     template_name = 'contacts/registro_usuario.html'


#     def form_valid(self, form):
#         if form.cleaned_data['contraseña'] != form.cleaned_data['confirmacioncontraseña']:
#             form.add_error('confirmacioncontraseña', 'Las contraseñas no coinciden.')
#             return self.form_invalid(form)
#         return super().form_valid(form)


# class RegistroUsuarioUpdateView(generic.UpdateView):
#     model = RegistroUsuario
#     fields = ('nombre','apellidopaterno','apellidomaterno','tipousuario','correo','contraseña','confirmacioncontraseña',)
#     success_url = reverse_lazy('registrousuario_list')
#     template_name = 'contacts/registro_usuario_form.html'

#     def form_valid(self, form):
#         if form.cleaned_data['contraseña'] != form.cleaned_data['confirmacioncontraseña']:
#             form.add_error('confirmacioncontraseña', 'Las contraseñas no coinciden.')
#             return self.form_invalid(form)
#         return super().form_valid(form)


# class RegistroUsuarioDeleteView(generic.DeleteView):
#     model = RegistroUsuario
#     success_url = reverse_lazy('registrousuario_list')
#     template_name='contacts/registro_usuario_confirm_delete.html'

# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from django.contrib.auth.views import LoginView
# from django.contrib import messages

# class CustomLoginView(LoginView):
#     template_name = "contacts/login.html"

#     def form_valid(self, form):
#         usuario = form.get_user()

#         if usuario.tipousuario == 'admin':
#             return redirect('MenuAdmin')  
#         elif usuario.tipousuario == 'ent':
#             return redirect('MenuEntrada') 
#         elif usuario.tipousuario == 'alm':
#             return redirect('MenuAlmacen')  
#         elif usuario.tipousuario == 'prod':
#             return redirect('MenuProduccion') 
#         elif usuario.tipousuario == 'cal':
#             return redirect('MenuCalidad') 
#         else:
#             return redirect('login') 

#     def form_invalid(self, form):
#         messages.error(self.request, "Usuario o contraseña incorrectos")
#         return super().form_invalid(form)


# CONTACTOS ---------------------------------------------

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
    paginate_by = 15  # Número de elementos por página

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
        "has_next": len(queryset) == items_per_page,  # Si quedan más páginas
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
    fields = ('materiaprima','loteseprisa','pesobruto','pesoneto','nocontenedores','claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe',)

    success_url = reverse_lazy('formato_recepcion_materia_prima')
    template_name='contacts/formato_recepcion_materia_prima_form.html'

class FormatoRecepcionMateriaPrimaUpdateView(generic.UpdateView):
    model = FormatoRecepcionMateriaPrima
    fields = ('materiaprima','loteseprisa','pesobruto','pesoneto','nocontenedores','claveproveedor','noanalisis','sku','noloteproveedor','fechacaducidad','recibe')
    success_url = reverse_lazy('formato_recepcion_materia_prima')
    template_name='contacts/formato_recepcion_materia_prima_form.html'

class FormatoRecepcionMateriaPrimaDeleteView(generic.DeleteView):
    model = FormatoRecepcionMateriaPrima
    success_url = reverse_lazy('formato_recepcion_materia_prima')
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

def export_orden_produccion_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/orden_produccion_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="OrdendeProduccion.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

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

class OrdenProduccionUpdateView(generic.UpdateView):
    model = DetalleOrden
    fields = ('skump', 'material', 'nolote', 'unidad','cantidad','surtio','verifico',)
    success_url = reverse_lazy('ordenproduccion_list')
    template_name='contacts/orden_produccion_form.html'

class OrdenProduccionDeleteView(generic.DeleteView):
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

        # Usar prefetch_related para obtener la relación 'kardexrecepcionmateriaprimaalmacen_set'
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
    
def export_control_aseguramiento_pdf(request):
    FormatoRecepcionMateriaPrimax = FormatoRecepcionMateriaPrima.objects.all()[:15]
    
    template_path = 'contacts/control_aseguramiento_calidad_pdf.html'
    context = {'FormatoRecepcionMateriaPrimax': FormatoRecepcionMateriaPrimax}

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
    FormatoBitacoraProductoTerminadox = FormatoBitacoraProductoTerminado.objects.all()[:15]
    
    template_path = 'contacts/formato_bitacora_producto_terminado_pdf.html'
    context = {'FormatoBitacoraProductoTerminadox': FormatoBitacoraProductoTerminadox}

    template = get_template(template_path)
    html = template.render(context)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="BitacoraProductoTerminado.pdf"'

    result = BytesIO()
    pdf = pisa.CreatePDF(BytesIO(html.encode("UTF-8")), dest=result)

    if pdf.err:
        return HttpResponse('Error generando el PDF', status=500)

    response.write(result.getvalue())
    return response

class kardex(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/kardex.html')
    


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
        Q(materiaprima__icontains=query) |
        Q(claveproveedor__icontains=query)
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


class GuardarKardexView(View):
    def post(self, request, *args, **kwargs):
        formato_id = request.POST.get('id')
        
        if not formato_id:
            return render(request, 'kardex.html', {'error': 'ID de formato no encontrado.'})

        formato_recepcion = get_object_or_404(FormatoRecepcionMateriaPrima, id=formato_id)

        fechasalida = request.POST.get('fecha_salida', None)
        if not fechasalida:
            return render(request, 'contacts/kardex.html', {'error': 'La fecha de salida es obligatoria.'})
        
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
                noloteproveedor=request.POST.get('lote_proveedor', ''),
                cantidadsale=request.POST.get('cantidad_sale', 0),  
                cantidadqueda=request.POST.get('cantidad_queda', 0),
                realizo=request.POST.get('realizo', ''),
                observaciones=request.POST.get('observaciones', ''), 

                formato_recepcion=formato_recepcion
            )
            kardex.save()
            return redirect('kardex_list') 
        except Exception as e:
            return render(request, 'contacts/kardex.html', {'error': f'No se pudo guardar el kardex: {e}'})

class KardexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'contacts/kardex.html')

from django.shortcuts import render, get_object_or_404
from .models import FormatoRecepcionMateriaPrima

def kardex_listlist(request):
    id = request.GET.get('id')

    if id:
        etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, pk=id)
        
        salidas = etiqueta.kardexrecepcionmateriaprimaalmacen_set.all()
        
        return render(request, 'contacts/kardex.html', {'etiqueta': etiqueta, 'salidas': salidas})
    else:
        return render(request, 'contacts/kardex.html', {'error': 'ID no proporcionado'})



# from django.shortcuts import render, get_object_or_404
# from .models import FormatoRecepcionMateriaPrima

# def kardex_listlist(request):
#     id = request.GET.get('id')

#     if id:
#         etiqueta = get_object_or_404(FormatoRecepcionMateriaPrima, pk=id)
        
#         salidas = etiqueta.kardexrecepcionmateriaprimaalmacen_set.all()
        
#         return render(request, 'contacts/kardex.html', {'etiqueta': etiqueta, 'salidas': salidas})
#     else:
#         return render(request, 'contacts/kardex.html', {'error': 'ID no proporcionado'})



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
