from django.urls import path
from locales import views

urlpatterns = [
    path('comercios/', views.Comercios.as_view(), name='comercios'),
    path('comercios/nuevo/', views.CrearComercio.as_view(), name='crear_comercio'),
    path('comercios/<int:pk>/', views.DetalleComercio.as_view(), name='detalle_comercio'),
    path('comercios/<int:pk>/editar/', views.EditarComercio.as_view(), name='editar_comercio'),
    path('comercios/<int:pk>/eliminar/', views.EliminarComercio.as_view(), name='eliminar_comercio'),   
]
 