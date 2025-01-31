from django.urls import path


from formatorecepcionmateriaalergenos import views

urlpatterns = [

    path('contacts/', views.contacts, name='contact_list'),


    path('', views.FormatoRecepcionMateriaAlargenosView.as_view(),name='formato_recepcion_materia'),
    path('new/', views.FormatoRecepcionMateriaAlergenosCreateView.as_view(),name='formatrecepcionmateriaalergenos_new'),
    path('<int:pk>/edit/', views.FormatoRecepcionMateriaAlergenosUpdateView.as_view(),name='formatorecepcionmateriaalergenos_edit'),
    path('<int:pk>/delete/', views.FormatoRecepcionMateriaAlergenosDeleteView.as_view(),name='formatorecepcionmaterialergenos_delete'),


]
