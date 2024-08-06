from django.urls import path
from .views import UsuarioCreateView,UsuarioListView,UsuarioDetailView,UsuarioUpdateView,UsuarioDeleteView

app_name = 'personas_app'
urlpatterns = [
    path('usuarios/agregar/', UsuarioCreateView.as_view(), name='usuarios-agregar'),
    path('usuarios/', UsuarioListView.as_view(), name='usuarios-list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuarios-detail'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuarios-edit'),
     path('usuarios/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuarios-delete'), 
]
