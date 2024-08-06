from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.db.models import Q  
from .models import Usuarios, Empleados
from .forms import UsuarioForm, UsuarioSearchForm, EmpleadosSearchForm, EmpleadoForm

class UsuarioCreateView(CreateView):
    model = Usuarios
    form_class = UsuarioForm
    template_name = 'personas/usuario_form.html'
    success_url = reverse_lazy('personas_app:usuarios-list')

class UsuarioListView(ListView):
    model = Usuarios
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = UsuarioSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            if query:
                queryset = queryset.filter(
                    Q(nombre__icontains=query) |
                    Q(apellido__icontains=query) |
                    Q(dni__icontains=query)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UsuarioSearchForm(self.request.GET)
        return context

class UsuarioDetailView(DetailView):
    model = Usuarios
    template_name = 'personas/usuario_detail.html'
    context_object_name = 'usuario'

class UsuarioUpdateView(UpdateView):
    model = Usuarios
    form_class = UsuarioForm
    template_name = 'personas/usuario_form.html'
    context_object_name = 'usuario'
    success_url = reverse_lazy('personas_app:usuarios-list')

class UsuarioDeleteView(DeleteView):
    model = Usuarios
    template_name = 'personas/usuario_confirm_delete.html'
    context_object_name = 'usuario'
    success_url = reverse_lazy('personas_app:usuarios-list')

#----------------------------------------Views Empleados--------------------------------------------------
# views.py

class EmpleadoCreateView(CreateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'personas/empleado_form.html'
    success_url = reverse_lazy('personas_app:empleados-list')

class EmpleadoListView(ListView):
    model = Empleados
    template_name = 'personas/empleado_list.html'
    context_object_name = 'empleados'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = EmpleadosSearchForm(self.request.GET)  # Asumiendo que tienes un formulario de búsqueda similar
        if form.is_valid():
            query = form.cleaned_data['query']
            if query:
                queryset = queryset.filter(
                    Q(nombre__icontains=query) |
                    Q(apellido__icontains=query) |
                    Q(dni__icontains=query)
                )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = EmpleadosSearchForm(self.request.GET)  # Asumiendo que tienes un formulario de búsqueda similar
        return context

class EmpleadoDetailView(DetailView):
    model = Empleados
    template_name = 'personas/empleado_detail.html'
    context_object_name = 'empleado'

class EmpleadoUpdateView(UpdateView):
    model = Empleados
    form_class = EmpleadoForm
    template_name = 'personas/empleado_form.html'
    context_object_name = 'empleado'
    success_url = reverse_lazy('personas_app:empleados-list')

class EmpleadoDeleteView(DeleteView):
    model = Empleados
    template_name = 'personas/empleado_confirm_delete.html'
    context_object_name = 'empleado'
    success_url = reverse_lazy('personas_app:empleados-list')

