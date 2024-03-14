from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from locales.models import Comercio
from django.contrib.auth.mixins import LoginRequiredMixin
 
class Comercios(ListView):
    model = Comercio
    context_object_name = 'comercios'
    template_name = "comercios/comercio.html"

class CrearComercio(CreateView):
    model = Comercio
    template_name = "comercios/crear_comercio.html"
    fields = ['representante_legal', 'nombre_comercio', 'fecha_apertura']
    success_url =  reverse_lazy('comercios')
    
class EliminarComercio(LoginRequiredMixin, DeleteView):
    model = Comercio 
    template_name = "comercios/eliminar_comercio.html"
    success_url =  reverse_lazy('comercios')
    
class EditarComercio(LoginRequiredMixin, UpdateView):
    model = Comercio
    template_name = "comercios/editar_comercio.html"
    success_url =  reverse_lazy('comercios')
    fields = ['representante_legal', 'nombre_comercio', 'fecha_apertura']
    
class DetalleComercio(DetailView):
     model = Comercio
     template_name = "comercios/detalle_comercio.html"
    
