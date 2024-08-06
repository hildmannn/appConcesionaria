from django.urls import path
from .views import VentasListView, VentasDetailView, VentasCreateView, VentasUpdateView, VentasDeleteView

app_name = 'ventas'

urlpatterns = [
    path('ventas/', VentasListView.as_view(), name='ventas_list'),
    path('<int:pk>/', VentasDetailView.as_view(), name='ventas_detail'),
    path('ventanew/', VentasCreateView.as_view(), name='ventas_create'),
    path('<int:pk>/editar/', VentasUpdateView.as_view(), name='ventas_update'),
    path('<int:pk>/eliminar/', VentasDeleteView.as_view(), name='ventas_delete'),
]
