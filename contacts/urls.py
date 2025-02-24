from django.urls import path

# from .views import generate_pdf
from contacts import views

from .views import tu_vista_guardar, buscar_etiqueta_identificacion_materiales, buscar_orden_produccion, buscar_material,buscar_kardex, PruebaTablaListView,kardex_listlist
# from .views import orden_produccion_view, menu_desplegable_view
from django.urls import path
# from .views import registro_usuario, login_usuario, menu_view, vista_protegida
from .views import menu_principal,RegistroUsuario, menu_admin,menu_entrada,register,menu_almacen,menu_produccion,menu_calidad

from django.contrib.auth.views import LogoutView
# from .views import LoginView,RegistroUsuariosListView,RegistroUsuariosEditView,RegistroUsuariosDeleteView,
from .views import LoginView,UserListView,UserEditView,UserDeleteView
# from .views import orden_produccion_view, agregar_detalle



urlpatterns = [
    #Vista contactos
    path('list', views.ContactListView.as_view(),name='contact_list'),
    path('new/', views.ContactCreateView.as_view(),name='contact_new'),
    path('<int:pk>/edit/', views.ContactUpdateView.as_view(),name='contact_edit'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(),name='contact_delete'),

    # path('', home, name='home'),
    path('', menu_principal, name='menu_principal'),
    # path('products/', products, name='products'),
    # path('registrousuarios/', RegistroUsuario, name='registro_usuarios'),
    # path('usuarios/', RegistroUsuariosListView.as_view(), name='registro_usuarios_list'),
    # path('usuarios/editar/<int:pk>/', RegistroUsuariosEditView.as_view(), name='registro_usuarios_edit'),
    # path('usuarios/eliminar/<int:pk>/', RegistroUsuariosDeleteView.as_view(), name='registro_usuarios_delete'),
    path('register/', register, name='register'),
    path('usuarios/', UserListView.as_view(), name='user_list'),
    path('usuarios/editar/<int:pk>/', UserEditView.as_view(), name='user_edit'),
    path('usuarios/eliminar/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path("Menu", views.Menu.as_view(),name='Menu'),

    path('login/', LoginView.as_view(), name='login'),

    path('menu_admin/', menu_admin, name='menu_admin'),
    path('menu_entrada/', menu_entrada, name='menu_entrada'),
    path('menu_almacen/', menu_almacen, name='menu_almacen'),
    path('menu_produccion/', menu_produccion, name='menu_produccion'),
    path('menu_calidad/', menu_calidad, name='menu_calidad'),    

    # path(" ", views.Menu.as_view(),name='Menu'),
    path("menuadmin/", views.MenuAdmin.as_view(),name='MenuAdmin'),
    path("menuentrada/", views.MenuEntrada.as_view(),name='MenuEntrada'),
    path("menualmacen/", views.MenuAlmacen.as_view(),name='MenuAlmacen'),
    path("menuproduccion/", views.MenuProduccion.as_view(),name='MenuProduccion'),
    path("menucalidad/", views.MenuCalidad.as_view(),name='MenuCalidad'),
    path("menupadmin/", views.MenuPAdmin.as_view(),name='MenuAdmin'),
    path("menupentrada/", views.MenuPEntrada.as_view(),name='MenuEntrada'),
    path("menupalmacen/", views.MenuPAlmacen.as_view(),name='MenuAlmacen'),
    path("menupproduccion/", views.MenuPProduccion.as_view(),name='MenuProduccion'),
    path("menupcalidad/", views.MenuPCalidad.as_view(),name='MenuCalidad'),

    # path('menu/', Menu, name='menu'),

    # Vista Formato Recepcion Materia Prima Alargenos
    path("fomatorecepcionmateria/", views.FormatoRecepcionMateriaAlergenosView.as_view(),name='formato_recepcion_materia'),
    path("formatorecepcionmateriaalergenos/", views.FormatoRecepcionMateriaAlergenosListView.as_view(),name='formatorecepcionmateriaalergenos_list'),
    path('formatorecepcionmateriaalergenos/new/', views.FormatoRecepcionMateriaAlergenosCreateView.as_view(),name='formatorecepcionmateriaalergenos_new'),
    path('formatorecepcionmateriaalergenos/<int:pk>/edit/',views.FormatoRecepcionMateriaAlergenosUpdateView.as_view(),name='formatorecepcionmateriaalergenos_edit'),
    path('formatorecepcionmateriaalergenos/<int:pk>/delete/',views.FormatoRecepcionMateriaAlergenosDeleteView.as_view(),name='formatorecepcionmateriaalergenos_delete'),
    # path("formatorecepcionmateriaalergenoslistview/",views.FormatoRecepcionMateriaAlergenosListViewView.as_view(),name='formatorecepcionmateriaalergenos_listview'),
    path('formatorecepcionmateriaalergenos/pdf/', views.export_formato_recepcion_materia_alergenos_pdf, name='export_formato_recepcion_materia_alergenos_pdf'),
    # path('pruebatabla/', PruebaTablaListView.as_view(), name='formato_recepcion_list'),
    path('formatorecepcionmateriaalergenosview/',views.FormatoRecepcionMateriaAlergenosListViewView.as_view(),name='formato_recepcion_materia_alergenos_view'),


    # Vista Formato Recepcion Material Empaque
    path("formatorecepcionmaterialempaque/", views.FormatoRecepcionMaterialEmpaqueView.as_view(),name='formato_recepcion_material_empaque'),
    path("formarorecepcionmaterialempaquelist/",views.FormatoRecepcionMaterialEmpaqueListView.as_view(),name='formatorecepcionmaterialempaque_list'),
    path('formatorecepcionmaterialempaque/new/', views.FormatoRecepcionMaterialEmpaqueCreateView.as_view(),name='formatorecepcionmaterialempaque_new'),
    path('formatorecepcionmaterialempaque/<int:pk>/edit/',views.FormatoRecepcionMaterialEmpaqueUpdateView.as_view(),name='formatorecepcionmaterialempaque_edit'),
    path('formatorecepcionmaterialempaque/<int:pk>/delete/',views.FormatoRecepcionMaterialEmpaqueDeleteView.as_view(),name='formatorecepcionmaterialempaque_delete'),
    # path("formarorecepcionmaterialempaquelistview/",views.FormatoRecepcionMaterialEmpaqueListViewView.as_view(),name='formatorecepcionmaterialempaque_listview'),
    path('formatorecepcionmaterialempaque/pdf/', views.export_formato_recepcion_material_empaque_pdf, name='export_formato_recepcion_material_empaque_pdf'),
    path('formatorecepcionmaterialempaqueview/',views.FormatoRecepcionMaterialEmpaqueListViewView.as_view(),name='formato_recepcion_material_empaque_view'),

    # path('registrousuarios/', views.RegistroUsuarioListView.as_view(), name='registrousuario_list'),
    # path('registrousuarios/new/', views.RegistroUsuarioCreateView.as_view(), name='registrousuario_new'),
    # path('registrousuarios/<int:pk>/edit/', views.RegistroUsuarioUpdateView.as_view(), name='registrousuario_edit'),
    # path('registrousuarios/<int:pk>/delete/', views.RegistroUsuarioDeleteView.as_view(), name='registrousuario_delete'),

    # # Vista Login
    # path("login/", views.LoginView.as_view(), name='login'),
    
    # path('login/', views.CustomLoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    # path('login/', views.LoginView.as_view(), name='login'),

    path('formatorecepcionmateriaprima/',views.FormatoRecepcionMateriaPrimaListView.as_view(),name='formato_recepcion_materia_prima'),
    path('formatorecepcionmateriaprima/new/', views.FormatoRecepcionMateriaPrimaCreateView.as_view(),name='formatorecepcionmateriaprima_new'),
    path('formatorecepcionmateriaprima/<int:pk>/edit/',views.FormatoRecepcionMateriaPrimaUpdateView.as_view(),name='formatorecepcionmateriaprima_edit'),
    path('formatorecepcionmateriaprima/<int:pk>/delete/',views.FormatoRecepcionMateriaPrimaDeleteView.as_view(),name='formatorecepcionmateriaprima_delete'),
    path('pruebatabla/', PruebaTablaListView.as_view(), name='formato_recepcion_list'),
    path('pruebatablas/', views.PruebaTablaView.as_view(),name='formato_recepcion_lists'),
    path('formatorecepcionmateriaprimaview/',views.FormatoRecepcionMateriaPrimaListViewView.as_view(),name='formato_recepcion_materia_prima_view'),

    # Vista Etiqueta Identificacion de Materiales
    path('etiq/', views.etiquetas.as_view(), name='etiquetas'),
    
    path('buscar/', buscar_etiqueta_identificacion_materiales, name='buscar_etiqueta'),
    path('guardar/', views.GuardarEtiquetaView.as_view(), name='guardar_etiqueta'),
    path('etiquetalist', views.EtiquetaIdentificacionMaterialesListView.as_view(),name='etiqueta_identificacion_materiales_list'),

    path('guardar/', tu_vista_guardar, name='tu_vista_guardar'), # FORMATOSOLICITUDANALISIS

    # Vista Orden de Produccion
    path('orden/', views.orden_produccion.as_view(), name='orden_produccion'),
    path('orden2/', views.orden_produccion2.as_view(),name='orden_produccion2'),
    path('exportordenproduccion/pdf/', views.export_orden_produccion_pdf, name='export_orden_produccion_pdf'),
    path('exportordenproduccion2/pdf/', views.export_orden_produccion2_pdf, name='export_orden_produccion2_pdf'),
    
    # Vista Etiqueta cuarentena
    path('etiquetacuarentena', views.Etiqueta_cuarentena.as_view(), name='etiqueta_cuarentena'),

    # Vista Kardex
    path('kardex/', views.kardex.as_view(), name='kardex'),
    path('kardex/pdf/', views.export_kardex_pdf, name='export_kardex_pdf'),
    path('kardex/list/',views.KardexListView.as_view(),name='kardex_list'),
    path('kardex/new/', views.KardexCreateView.as_view(),name='kardex_new'),
    path('kardex/<int:pk>/edit/',views.KardexUpdateView.as_view(),name='kardex_edit'),
    path('kardex/<int:pk>/delete/',views.KardexDeleteView.as_view(),name='kardex_delete'),
    path('kardex/buscar/', buscar_kardex, name='buscar_kardex'),
    # path('guardar-kardex/', guardar_kardex, name='guardar_kardex'),
    path('kardex/guardar/', views.GuardarKardexView.as_view(), name='guardar_kardex'),
    path('kardexview/',views.KardexListViewView.as_view(),name='kardex_view'),
    path('exportkardex/pdf/', views.export_formato_kardex_pdf2, name='export_formato_kardex_pdf2'),
    path('kardexlist/', kardex_listlist, name='kardex_listlist'),

    # path('download-pdf/', views.generate_pdf.as_view(), name='download_pdf'),

    path('export/pdf/', views.export_contacts_pdf, name='export_contacts_pdf'),
    # path('export-pdf/', export_formato_recepcion_materia_prima_pdf, name='export_formato_recepcion_msteria_prima_pdf'),
    path('exportformatorecepcionmateriaprima/pdf/', views.export_formato_recepcion_materia_prima_pdf, name='export_formato_recepcion_msteria_prima_pdf'),
    path('exportetiquetaidentificacionmateriales/pdf', views.export_etiqueta_identificacion_materiales_pdf, name='export_etiqueta_identificacion_materiales_pdf'),
    path('exportetiquetacuarentena/pdf', views.export_etiqueta_cuarentena_pdf, name='export_etiqueta_cuarentena_pdf'),
    path('exportformatosolicitudanalisis/pdf', views.export_formato_solicitud_analisis_pdf, name='export_formato_solicitud_analisis_pdf'),

    # Vista Formato Solicitud de Analisis
    path('formatosolicitudanalisis/', views.FormatoSolicitudAnalisisView.as_view(), name='formato_solicitud_analisis'),
    path('exportformatosolicitudanalisis/pdf/', views.export_formato_solicitud_analisis_pdf, name='export_formato_solicitud_analisis_pdf'),
    path('materiaprima/details/', views.get_materia_prima_details, name='get_materia_prima_details'),
    path('buscar_solicitud_analisis/', views.buscar_solicitud_analisis, name='buscar_solicitud_analisis'),

    #Vista Orden de Produccion
    path('ordenproduccionview/', views.OrdenProduccionView.as_view(), name='orden_produccion_view'),
    path('ordenproduccion/list', views.OrdenProduccionListView.as_view(),name='ordenproduccion_list'),
    path('ordenproduccion/new/', views.OrdenProduccionCreateView.as_view(),name='ordenproduccion_new'),
    path('ordenproduccionlist/new/', views.OrdenProduccionCreateListView.as_view(),name='ordenproduccion_newlist'),
    path('ordenproduccionlist/<int:pk>/edit/', views.OrdenProduccionUpdateView.as_view(),name='ordenproduccion_edit'),
    path('ordenproduccionlist/<int:pk>/delete/', views.OrdenProduccionDeleteView.as_view(),name='ordenproduccion_delete'),
    path('buscar-orden/', buscar_orden_produccion, name='buscar_orden_produccion'),
    path('buscar-material/', buscar_material, name='buscar_material'),
    path('detalleorden/new/', views.DetalleOrdenCreateListView.as_view(),name='detalleorden_new'),
    path('ordenproduccionlists',views.OrdenProduccionList.as_view(),name='ordenproduccionlist'),
    path('ordenproduccionviewv/',views.OrdenProduccionListViewView.as_view(),name='ordenproduccion_view'),
    # path("orden-produccion/", orden_produccion_view, name="orden_produccion"),
    # path("agregar-detalle/", agregar_detalle, name="agregar_detalle"),

    # Vista Control de Aseguramiento
    path('controlaseguramientoview/', views.ControlAseguramientoView.as_view(), name='control_aseguramiento_view'),
    path('controlaseguramientopdf/pdf/', views.export_control_aseguramiento_pdf, name='export_control_aseguramiento_pdf'),
    path('controlaseguramientopdf2/pdf/', views.export_control_aseguramiento2_pdf, name='export_control_aseguramiento_pdf2'),

    # Menu
    path('menupview/', views.MenuPView.as_view(), name='menu_p_view'),
    path('menuprview/', views.MenuPrView.as_view(), name='menu_pr_view'),

    path('bitacoraproductoterminadoview/', views.FormatoBitacoraProductoTerminadoView.as_view(), name='bitacora_producto_terminado_view'),
    path('bitacoraproductoterminadopdf/pdf/', views.export_bitacora_producto_terminado_pdf, name='export_bitacora_producto_terminado_pdf'),
    
    path('bitacoraproductoterminado/',views.FormatoBitacoraProductoTerminadoListView.as_view(),name='formato_bitacora_producto_terminado'),
    path('bitacoraproductoterminado/new/', views.FormatoBitacoraProductoTerminadoCreateView.as_view(),name='formatobitacoraproductoterminado_new'),
    path('bitacoraproductoterminado/<int:pk>/edit/',views.FormatoBitacoraProductoTerminadoUpdateView.as_view(),name='formatobitacoraproductoterminado_edit'),
    path('bitacoraproductoterminado/<int:pk>/delete/',views.FormatoBitacoraProductoTerminadoDeleteView.as_view(),name='formatobitacoraproductoterminado_delete'),
    path('bitacoraproductoterminadoviewview/', views.FormatoBitacoraProductoTerminadoListViewView.as_view(),name='formato_bitacora_producto_terminado_view')

]
