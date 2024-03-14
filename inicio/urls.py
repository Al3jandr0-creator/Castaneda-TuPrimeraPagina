from django.urls import path
from inicio.views import inicio, mostrar_horario, crear_cliente, clientes, ver_cliente, eliminar_cliente, editar_cliente, acerca_de_mi

urlpatterns = [
    path('', inicio, name='inicio'),
    path('acercademi/', acerca_de_mi, name='acerca_de_mi'),
    path('mostrar-horario/', mostrar_horario, name='mostrar_horario'),
    path('clientes/', clientes, name='clientes'),
    path('clientes/nuevo/', crear_cliente, name='crear_cliente'),
    path('clientes/<int:id_cliente>/', ver_cliente, name='ver_cliente'),
    path('clientes/<int:id_cliente>/eliminar/', eliminar_cliente, name='eliminar_cliente'),
    path('clientes/<int:id_cliente>/editar/', editar_cliente, name='editar_cliente'),
]