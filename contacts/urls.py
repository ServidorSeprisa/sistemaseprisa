from django.urls import path

from contacts import views

from .views import tu_vista_guardar, buscar_etiqueta_identificacion_materiales, buscar_orden_produccion, buscar_material, PruebaTablaListView,kardex_listlist
from django.urls import path
from .views import menu_principal,RegistroUsuario, menu_admin,menu_entrada,register,menu_almacen,menu_produccion,menu_calidad

from django.contrib.auth.views import LogoutView
from .views import LoginView,UserListView,UserEditView,UserDeleteView
from .views import guardar_muestras, buscar_orden,control_aseguramiento_calidad_list,ControlaseguramientocalidadListView,obtener_orden_produccion,buscar_ordenproduccion
from .views import ordenproduccion_new, kardex_prodlist,OrdenProduccionView,ver_notificaciones, marcar_notificacion_leida, OrdenProduccionViewList,ControlaseguramientocalidadListViewV,buscar_orden_produccion_view
from .views import EditarDetalleOrdenView, EliminarDetalleOrdenView

urlpatterns = [
    #Vista contactos
    path('list', views.ContactListView.as_view(),name='contact_list'),
    path('new/', views.ContactCreateView.as_view(),name='contact_new'),
    path('<int:pk>/edit/', views.ContactUpdateView.as_view(),name='contact_edit'),
    path('<int:pk>/delete/', views.ContactDeleteView.as_view(),name='contact_delete'),

    # Usuarios
    path('register/', register, name='register'), #si
    path('usuarios/', UserListView.as_view(), name='user_list'), #si
    path('usuarios/editar/<int:pk>/', UserEditView.as_view(), name='user_edit'),
    path('usuarios/eliminar/<int:pk>/', UserDeleteView.as_view(), name='user_delete'), #si

    # Login
    path('login/', LoginView.as_view(), name='login'), #si

    # Menús
    path('', menu_principal, name='menu_principal'),

    path("Menu", views.Menu.as_view(),name='Menu'),
    path('menu_admin/', menu_admin, name='menu_admin'),
    path('menu_entrada/', menu_entrada, name='menu_entrada'),
    path('menu_almacen/', menu_almacen, name='menu_almacen'),
    path('menu_produccion/', menu_produccion, name='menu_produccion'),
    path('menu_calidad/', menu_calidad, name='menu_calidad'),    

    # Vista Formato Recepción Materia Prima
    path('pruebatabla/', PruebaTablaListView.as_view(), name='formato_recepcion_list'), #si 
    path('formatorecepcionmateriaprima/new/', views.FormatoRecepcionMateriaPrimaCreateView.as_view(),name='formatorecepcionmateriaprima_new'), #si
    path('formatorecepcionmateriaprima/<int:pk>/edit/',views.FormatoRecepcionMateriaPrimaUpdateView.as_view(),name='formatorecepcionmateriaprima_edit'), #si
    path('formatorecepcionmateriaprima/<int:pk>/delete/',views.FormatoRecepcionMateriaPrimaDeleteView.as_view(),name='formatorecepcionmateriaprima_delete'), #si
    path('descargar_etiqueta/<int:pk>/', views.descargar_etiqueta, name='descargar_etiqueta'),
    path('formatorecepcionmateriaprimaview/',views.FormatoRecepcionMateriaPrimaListViewView.as_view(),name='formato_recepcion_materia_prima_view'), #si
    path('exportformatorecepcionmateriaprima/pdf/', views.export_formato_recepcion_materia_prima_pdf, name='export_formato_recepcion_msteria_prima_pdf'), #si

    # Vista Formato Recepcion Material Empaque
    path("formatorecepcionmaterialempaque/", views.FormatoRecepcionMaterialEmpaqueView.as_view(),name='formato_recepcion_material_empaque'),
    path("formarorecepcionmaterialempaquelist/",views.FormatoRecepcionMaterialEmpaqueListView.as_view(),name='formatorecepcionmaterialempaque_list'), #si
    path('formatorecepcionmaterialempaque/new/', views.FormatoRecepcionMaterialEmpaqueCreateView.as_view(),name='formatorecepcionmaterialempaque_new'), #si
    path('formatorecepcionmaterialempaque/<int:pk>/edit/',views.FormatoRecepcionMaterialEmpaqueUpdateView.as_view(),name='formatorecepcionmaterialempaque_edit'), #si
    path('formatorecepcionmaterialempaque/<int:pk>/delete/',views.FormatoRecepcionMaterialEmpaqueDeleteView.as_view(),name='formatorecepcionmaterialempaque_delete'), #si
    path('formatorecepcionmaterialempaque/pdf/', views.export_formato_recepcion_material_empaque_pdf, name='export_formato_recepcion_material_empaque_pdf'), #si
    path('formatorecepcionmaterialempaqueview/',views.FormatoRecepcionMaterialEmpaqueListViewView.as_view(),name='formato_recepcion_material_empaque_view'), #si

    # Vista Formato Recepcion Materia Prima Alergenos
    path("fomatorecepcionmateria/", views.FormatoRecepcionMateriaAlergenosView.as_view(),name='formato_recepcion_materia'),
    path("formatorecepcionmateriaalergenos/", views.FormatoRecepcionMateriaAlergenosListView.as_view(),name='formatorecepcionmateriaalergenos_list'), #si
    path('formatorecepcionmateriaalergenos/new/', views.FormatoRecepcionMateriaAlergenosCreateView.as_view(),name='formatorecepcionmateriaalergenos_new'), #si
    path('formatorecepcionmateriaalergenos/<int:pk>/edit/',views.FormatoRecepcionMateriaAlergenosUpdateView.as_view(),name='formatorecepcionmateriaalergenos_edit'), #si
    path('formatorecepcionmateriaalergenos/<int:pk>/delete/',views.FormatoRecepcionMateriaAlergenosDeleteView.as_view(),name='formatorecepcionmateriaalergenos_delete'), #si 
    path('formatorecepcionmateriaalergenos/pdf/', views.export_formato_recepcion_materia_alergenos_pdf, name='export_formato_recepcion_materia_alergenos_pdf'), #si
    path('formatorecepcionmateriaalergenosview/',views.FormatoRecepcionMateriaAlergenosListViewView.as_view(),name='formato_recepcion_materia_alergenos_view'), # si

    # Vista Kardex
    path('kardexview/',views.KardexListViewView.as_view(),name='kardex_view'), #si
    path('kardexlist/', kardex_listlist, name='kardex_listlist'), #si
    path('kardex/<int:pk>/edit/',views.KardexUpdateView.as_view(),name='kardex_edit'), # si
    path('kardex/<int:pk>/delete/',views.KardexDeleteView.as_view(),name='kardex_delete'), #si
    path('kardex/guardar/', views.GuardarKardexView.as_view(), name='guardar_kardex'), #si
    path('kardex/pdf/', views.export_kardex_pdf, name='export_kardex_pdf'), #si
    path('kardexvview/',views.KardexListVView.as_view(),name='kardex_vview'), #si
    path('kardexprodlist/', kardex_prodlist, name='kardex_prodlist'), #si
    path('kardexprod/guardar/', views.GuardarKardexProdView.as_view(), name='guardar_kardexprod'), #si
    path('exportkardex/pdf/', views.export_formato_kardex_pdf2, name='export_formato_kardex_pdf2'), #si

    # Bitácora De Producto Terminado
    # path('bitacoraproductoterminadoview/', views.FormatoBitacoraProductoTerminadoView.as_view(), name='bitacora_producto_terminado_view'),
    path('bitacoraproductoterminadopdf/pdf/', views.export_bitacora_producto_terminado_pdf, name='export_bitacora_producto_terminado_pdf'),
    
    path('bitacoraproductoterminado/',views.FormatoBitacoraProductoTerminadoListView.as_view(),name='formato_bitacora_producto_terminado'), #si
    path('bitacoraproductoterminado/new/', views.FormatoBitacoraProductoTerminadoCreateView.as_view(),name='formatobitacoraproductoterminado_new'), #si 
    path('bitacoraproductoterminado/<int:pk>/edit/',views.FormatoBitacoraProductoTerminadoUpdateView.as_view(),name='formatobitacoraproductoterminado_edit'), # si
    path('bitacoraproductoterminado/<int:pk>/delete/',views.FormatoBitacoraProductoTerminadoDeleteView.as_view(),name='formatobitacoraproductoterminado_delete'), #si
    path('bitacoraproductoterminadoviewview/', views.FormatoBitacoraProductoTerminadoListViewView.as_view(),name='formato_bitacora_producto_terminado_view'), #si
    # path('bitacoraproductoterminadoviewvv/',views.BitacoraProductoterminadoListViewView.as_view(),name='bitacoraproductoterminado_view'),


    # Vista Orden de Producción

    path('ordenproduccionlistview/', views.OrdenProduccionListView.as_view(), name='orden_produccion_list_view'), #si
    path('orden-produccion/<int:pk>/', OrdenProduccionViewList.as_view(), name='ordenproduccionviewlist'), #si
    path('exportordenproduccioncreatelistview/pdf/<int:pk>/', views.export_orden_produccion_create_listview_pdf, name='export_orden_produccion_create_listview_pdf'),

    path('ordenproduccioncreate/',views.OrdenProduccionView.as_view(),name='ordenproduccionview'), #si
    path("ordenproduccion-create/", ordenproduccion_new, name="ordenproduccion_create"), #si
    path('kardexprodlist/', kardex_prodlist, name='kardex_prodlist'), #si
    path('kardexprod/guardar/', views.GuardarKardexProdView.as_view(), name='guardar_kardexprod'), #si
    path('exportkardex/pdf/', views.export_formato_kardex_pdf2, name='export_formato_kardex_pdf2'), #si
    path('editar-detalle-orden/', EditarDetalleOrdenView.as_view(), name='editar_detalle_orden'),#si
    path('eliminar-detalle-orden/', EliminarDetalleOrdenView.as_view(), name='eliminar_detalle_orden'), #si
    path('ordenproduccionlistviewv', views.OrdenProduccionListViewV.as_view(),name='orden_produccion_list_viewv'), # si
    path('ordenproduccionlistvieww/', views.OrdenProduccionListListView.as_view(), name='orden_produccion_list_vieww'),

    # Control de Aseguramiento de Calidad
    
    path('controlaseguramientoview/', views.ControlAseguramientoView.as_view(), name='control_aseguramiento_view'),
    path('controlaseguramientopdf/pdf/', views.export_control_aseguramiento_pdf, name='export_control_aseguramiento_pdf'),
    path('controlaseguramientopdf2/pdf/<int:orden_produccion_id>/', views.export_control_aseguramiento2_pdf, name='export_control_aseguramiento_pdf2'),

    path('buscar-ordenproduccionviewv/', buscar_orden_produccion, name='ordenproduccion_search'), #si
    path('buscar-ordenproduccionviewvv/', buscar_orden_produccion_view, name='ordenproduccion_searchv'), #si
    path('guardar_muestras/', views.guardar_muestras, name='guardar_muestras'),
    path('buscar_orden/', buscar_orden, name='buscar_orden'),

    # Notificaciones
    path('notificaciones/', views.ver_notificaciones, name='ver_notificaciones'), #si
    path('notificacion/leida/<int:notificacion_id>/', views.marcar_notificacion_leida, name='marcar_notificacion_leida'), #si
    path('notificacion/redirigir/<int:notificacion_id>/', views.redirigir_a_orden, name='redirigir_a_orden'), #si

     # Vista Etiqueta Identificacion de Materiales
    path('etiq/', views.etiquetas.as_view(), name='etiquetas'),
    path('descargar_etiqueta/<int:pk>/', views.descargar_etiqueta, name='descargar_etiqueta'),

    # ------------------------------------------------------------------------------------------------------------------------------
    
    path('buscar/', buscar_etiqueta_identificacion_materiales, name='buscar_etiqueta'),
    path('guardar/', views.GuardarEtiquetaView.as_view(), name='guardar_etiqueta'),
    path('etiquetalist', views.EtiquetaIdentificacionMaterialesListView.as_view(),name='etiqueta_identificacion_materiales_list'),

    path('guardar/', tu_vista_guardar, name='tu_vista_guardar'), # FORMATOSOLICITUDANALISIS

    # Vista Etiqueta cuarentena
    path('etiquetacuarentena', views.Etiqueta_cuarentena.as_view(), name='etiqueta_cuarentena'),
    path('exportetiquetacuarentena/pdf', views.export_etiqueta_cuarentena_pdf, name='export_etiqueta_cuarentena_pdf'),

    path('controlaseguramientolist/', control_aseguramiento_calidad_list,name='control_aseguramiento_calidad_list'),
    path('controlaseguramientolists/', ControlaseguramientocalidadListView.as_view(), name='control_aseguramiento_list'),
    path('controlaseguramientolistv/', ControlaseguramientocalidadListViewV.as_view(), name='control_aseguramiento_listv'),

    path('obtener-orden-produccion/<str:no_orden>/', obtener_orden_produccion, name='obtener_orden_produccion'),

    path('ordenproduccionview/', views.OrdenProduccionView.as_view(), name='orden_produccion_view'),
    path('ordenproduccion/list', views.OrdenProduccionListView.as_view(),name='ordenproduccion_list'),
    path('ordenproduccion/new/', views.OrdenProduccionCreateView.as_view(),name='ordenproduccion_new'),
    path('ordenproduccionlist/new/', views.OrdenProduccionCreateListView.as_view(),name='ordenproduccion_newlist'),
    path('ordenproduccionlist/<int:pk>/edit/', views.OrdenProduccionUpdateView.as_view(),name='ordenproduccion_edit'),
    path('ordenproduccionlist/<int:pk>/delete/', views.OrdenProduccionDeleteView.as_view(),name='ordenproduccion_delete'),
    path('buscarorden/', buscar_ordenproduccion, name='buscar_ordenproduccion'),
    path('ordenproduccionviewv/', buscar_ordenproduccion, name='ordenproduccionsearch'),

    path('buscar-orden/', buscar_orden_produccion, name='buscar_orden_produccion'),
    path('buscar-material/', buscar_material, name='buscar_material'),
    path('detalleorden/new/', views.DetalleOrdenCreateListView.as_view(),name='detalleorden_new'),
    path('ordenproduccionlists',views.OrdenProduccionList.as_view(),name='ordenproduccionlist'),
    path('ordenproduccionviewv/',views.OrdenProduccionListViewView.as_view(),name='ordenproduccion_view'),

    path('ordenproduccionviewvv/',views.OrdenProduccionListViewViewV.as_view(),name='ordenproduccion_viewv'),
    # path('registrar_salida/<int:orden_id>/<int:kardex_id>/', views.registrar_salida, name='registrar_salida'),
    path('guardar_detalle_orden/<int:orden_id>/', views.guardar_detalle_orden, name='guardar_detalle_orden'),
    path('ordenproduccion/<int:kardex_id>/', OrdenProduccionView.as_view(), name='ordenproduccionview_kardex'),
    path('ordenproduccionlistviewlist', views.OrdenProduccionListList.as_view(),name='ordenproduccion_listlist'),


    # Vista Orden de Produccion
    path('orden/', views.orden_produccion.as_view(), name='orden_produccion'),
    path('orden2/', views.orden_produccion2.as_view(),name='orden_produccion2'),
    path('exportordenproduccion/pdf/', views.export_orden_produccion_pdf, name='export_orden_produccion_pdf'),

    path('exportordenproduccion2/pdf/', views.export_orden_produccion2_pdf, name='export_orden_produccion2_pdf'),
    path('exportordenproduccion3/pdf/', views.export_ordenes_produccion_pdf, name='export_ordenes_produccion_pdf'),


    path('export/pdf/', views.export_contacts_pdf, name='export_contacts_pdf'),
    path('exportetiquetaidentificacionmateriales/pdf', views.export_etiqueta_identificacion_materiales_pdf, name='export_etiqueta_identificacion_materiales_pdf'), #si
    path('exportetiquetacuarentena/pdf', views.export_etiqueta_cuarentena_pdf, name='export_etiqueta_cuarentena_pdf'),
    path('exportformatosolicitudanalisis/pdf', views.export_formato_solicitud_analisis_pdf, name='export_formato_solicitud_analisis_pdf'),

    # Vista Formato Solicitud de Analisis
    path('formatosolicitudanalisis/', views.FormatoSolicitudAnalisisView.as_view(), name='formato_solicitud_analisis'),
    path('exportformatosolicitudanalisis/pdf/', views.export_formato_solicitud_analisis_pdf, name='export_formato_solicitud_analisis_pdf'),
    path('materiaprima/details/', views.get_materia_prima_details, name='get_materia_prima_details'),
    path('buscar_solicitud_analisis/', views.buscar_solicitud_analisis, name='buscar_solicitud_analisis'),

    #Vista Orden de Produccion

    path('menupview/', views.MenuPView.as_view(), name='menu_p_view'),
    path('menuprview/', views.MenuPrView.as_view(), name='menu_pr_view'),

    # Notificaciones
    path('notificaciones/', views.ver_notificaciones, name='ver_notificaciones'), #si
    path('notificacion/leida/<int:notificacion_id>/', views.marcar_notificacion_leida, name='marcar_notificacion_leida'), #si
    path('notificacion/redirigir/<int:notificacion_id>/', views.redirigir_a_orden, name='redirigir_a_orden'), #si

    path('descargar_control/', views.descargar_control, name='descargar_control'),
    path('descargar_control/', views.descargar_control, name='descargar_control'),
    path('descargar-control/', views.descargar_control, name='descargar_control_alt'), 

]
