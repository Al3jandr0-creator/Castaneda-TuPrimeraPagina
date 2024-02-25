from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from locales.models import Comercio
from django.urls import reverse_lazy

   
class Comercios(ListView):
    model = Comercio
    context_object_name = 'comercio'
    template_name = "comercios/comercio.html"


class CrearComercio(CreateView):
    model = Comercio
    template_name = "comercios/crear_comercio.html"
    fields = ['representante_legal', 'nombre_comercio', 'fecha_apertura']
    success_url =  reverse_lazy('comercios')