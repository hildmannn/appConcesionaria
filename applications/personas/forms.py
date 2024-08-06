from django import forms
from .models import Usuarios

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'direccion', 'telefono', 'dni', 'mail']

class UsuarioSearchForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=100, required=False)