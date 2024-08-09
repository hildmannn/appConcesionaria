from django.urls import path
from .views import UsuarioCreateView, UsuarioListView, UsuarioDetailView, UsuarioUpdateView, UsuarioDeleteView, EmpleadoCreateView, EmpleadoListView, EmpleadoDetailView, EmpleadoUpdateView, EmpleadoDeleteView

app_name = 'personas_app'
urlpatterns = [
    path('usuarios/agregar/', UsuarioCreateView.as_view(), name='usuarios-agregar'),
    path('usuarios/', UsuarioListView.as_view(), name='usuarios-list'),
    path('usuarios/<int:pk>/', UsuarioDetailView.as_view(), name='usuarios-detail'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuarios-edit'),
    path('usuarios/<int:pk>/eliminar/', UsuarioDeleteView.as_view(), name='usuarios-delete'),
    path('empleados/', EmpleadoListView.as_view(), name='empleados-list'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleados-create'),
    path('empleados/<int:pk>/', EmpleadoDetailView.as_view(), name='empleados-detail'),
    path('empleados/<int:pk>/editar/', EmpleadoUpdateView.as_view(), name='empleados-update'),
    path('empleados/<int:pk>/eliminar/', EmpleadoDeleteView.as_view(), name='empleados-delete'),
]
