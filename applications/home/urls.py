from django.urls import path
from . import views

app_name = 'home_app'

urlpatterns = [
    path('', views.home_view, name='home'),  
    path('vehiculosList/', views.VehiculosListView.as_view(), name='vehiculos-list'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    #path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    #path('empleado_dashboard/', views.empleado_dashboard, name='empleado_dashboard'),
    #path('usuario_dashboard/', views.usuario_dashboard, name='usuario_dashboard'),
    
   
]
