from django import forms

class FormularioBaseCliente(forms.Form):
    nombre= forms.CharField(max_length = 20)
    apellido= forms.CharField(max_length = 30)
    edad= forms.IntegerField()
    
class FormularioCreacionCliente(FormularioBaseCliente):
    ...

class FormularioEdicionCliente(FormularioBaseCliente):
    gastos = forms.IntegerField()
     
class FormularioBusquedaCliente(forms.Form):
    nombre= forms.CharField(max_length = 20, required=False)
   