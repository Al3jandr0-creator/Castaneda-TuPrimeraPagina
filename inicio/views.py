from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import Template 
from inicio.models import Cliente
import random
from inicio.forms import FormularioCreacionCliente

def inicio(request):
    return render(request, 'inicio.html')

def clientes(request):
    clientes =Cliente.objects.all()
    return render(request, 'clientes.html', {'clientes':clientes} )

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
        
    return render(request, 'crear_cliente.html', {'formulario':formulario})