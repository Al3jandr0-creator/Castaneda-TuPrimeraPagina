from django.urls import path
from locales import views

urlpatterns = [
    path('comercios/', views.Comercios.as_view(), name='comercios'),
    path('comercios/nuevo/', views.CrearComercio.as_view(), name='crear_comercio')
]
 