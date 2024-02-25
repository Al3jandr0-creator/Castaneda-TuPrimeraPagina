from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template 
from inicio.models import Cliente
import random
from inicio.forms import FormularioCreacionCliente, FormularioBusquedaCliente, FormularioEdicionCliente

def inicio(request):
    return render(request, 'inicio/inicio.html')

 
def clientes(request):
    formulario = FormularioBusquedaCliente(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data.get('nombre')
        clientes = Cliente.objects.filter(nombre__icontains=nombre_a_buscar)
    return render(request, 'inicio/clientes.html', {'clientes':clientes, 'formulario':formulario})

def mostrar_horario(request):
    fecha = datetime.now()
    return HttpResponse(f'Esta es la fecha y hora actual: {fecha}')

def crear_cliente(request):
    formulario = FormularioCreacionCliente()
    if request.method == "POST":
        formulario = FormularioCreacionCliente(request.POST)
        if formulario.is_valid():
            nombre = formulario.cleaned_data.get('nombre')
            apellido = formulario.cleaned_data.get('apellido')
            edad = formulario.cleaned_data.get('edad')
            gastos = random.randint(100,1000)
            cliente = Cliente(nombre=nombre, apellido=apellido, edad=edad, gastos= random.randint(100, 1000))
            cliente.save()
            return redirect('clientes')
        
    return render(request, 'inicio/crear_cliente.html', {'formulario':formulario})

def eliminar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    cliente.delete()
    return redirect('clientes')
    
def editar_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    formulario = FormularioEdicionCliente(initial={'nombre': cliente.nombre, 'apellido': cliente.apellido, 'edad':cliente.edad, 'gastos':cliente.gastos})
    
    if request.method == 'POST':
       formulario = FormularioEdicionCliente(request.POST)
       if formulario.is_valid():      
           info_nueva = formulario.cleaned_data
           cliente.nombre = info_nueva.get('nombre')
           cliente.apellido = info_nueva.get('apellido')
           cliente.edad = info_nueva.get('edad')
           cliente.gastos = info_nueva.get('gastos')
           cliente.save()
           return redirect('clientes')
           
    return render(request, 'inicio/editar_cliente.html', {'cliente': cliente, 'formulario': formulario})

def ver_cliente(request, id_cliente):
    cliente = Cliente.objects.get(id=id_cliente)
    return render(request, 'inicio/ver_cliente.html', {'cliente': cliente}) 