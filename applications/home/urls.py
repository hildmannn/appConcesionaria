# home/urls.py
from django.urls import path
from . import views


app_name = 'home_app'
urlpatterns = [
    path('', views.home_view, name='home'),  # Ruta para la página de inicio
    path('nosotros/', views.nosotros, name='nosotros'),
    path('vehiculosList/', views.VehiculosListView.as_view(), name='vehiculos-list'),
]
