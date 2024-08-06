from django import forms
from .models import Ventas

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = ['vehiculo', 'cliente', 'empleado', 'fecha', 'medioPago', 'cuotas', 'interes', 'montoFinanciado']
        widgets = {
            'fecha': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
