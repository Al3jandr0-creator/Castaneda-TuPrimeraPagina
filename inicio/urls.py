from django.urls import path
from inicio.views import inicio, mostrar_horario, crear_cliente, clientes

urlpatterns = [
    path('', inicio, name='inicio'),
    path('mostrar-horario/', mostrar_horario, name='mostrar_horario'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/nuevo/', crear_cliente, name='crear_cliente'),   
]