from django.urls import path
from .views import VehiculosDisponiblesView, VehiculoDetailView

app_name = 'vehiculos_app'
urlpatterns = [
    path('vehiculos/', VehiculosDisponiblesView.as_view(), name='vehiculos_disponibles'),
    path('vehiculos/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo_detalle'),
]
