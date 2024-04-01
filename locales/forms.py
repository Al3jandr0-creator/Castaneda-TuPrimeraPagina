from django import forms
from .models import Comercio

class CrearComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = ['representante_legal', 'nombre_comercio', 'fecha_apertura', 'imagen']
