from django import forms
from .models import Marcas, Categorias

class VehiculoSearchForm(forms.Form):
    query = forms.CharField(required=False, label='Buscar por modelo o marca')
    marca = forms.ModelChoiceField(queryset=Marcas.objects.all(), required=False, label='Marcas')
    categoria = forms.ModelChoiceField(queryset=Categorias.objects.all(), required=False, label='Categoría')
    km_min = forms.IntegerField(label='Km mínimo', required=False)
    km_max = forms.IntegerField(label='Km máximo', required=False)
    año_min = forms.IntegerField(label='Año mínimo', required=False)
    año_max = forms.IntegerField(label='Año máximo', required=False)
    precio_min = forms.IntegerField(label='Precio mínimo', required=False)
    precio_max = forms.IntegerField(label='Precio máximo', required=False)
