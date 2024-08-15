from django.urls import path
from .views import *

app_name = 'vehiculos_app'
urlpatterns = [
    path('vehiculos/', VehiculosDisponiblesView.as_view(), name='vehiculos-disponibles'),
    path('vehiculos/<int:pk>/', VehiculoDetailView.as_view(), name='vehiculo_detalle'),
    path('vehiculo/crear/', VehiculoCreateView.as_view(), name='vehiculo-create'),
    path('modelo/crear/', ModeloCreateView.as_view(), name='modelo-create'),
    path('proveedor/crear/', ProveedorCreateView.as_view(), name='proveedor-create'),
    path('categoria/crear/', CategoriaCreateView.as_view(), name='categoria-create'),
    path('marca/crear/', MarcaCreateView.as_view(), name='marca-create'),
    path('ficha-tecnica/crear/', FichaTecnicaCreateView.as_view(), name='ficha-tecnica-create'),
    path('vehiculos/lista-admin/', VehiculosListAdminView.as_view(), name='vehiculo-list'),
    path('vehiculos/<int:pk>/eliminar/', VehiculoDeleteView.as_view(), name='vehiculo-delete'),
    
]
