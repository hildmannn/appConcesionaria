from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Vehiculo, Modelos,Marcas, Categorias, FichasTecnicas
from applications.inventario.models import Proveedor
from .forms import VehiculoSearchForm, ModelosForm, VehiculoForm
from django.contrib.staticfiles.storage import staticfiles_storage

class VehiculosDisponiblesView(ListView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculos_disponibles.html'
    context_object_name = 'vehiculos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = VehiculoSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            marca = form.cleaned_data['marca']
            categoria = form.cleaned_data['categoria']
            km_min = form.cleaned_data['km_min']
            km_max = form.cleaned_data['km_max']
            año_min = form.cleaned_data['año_min']
            año_max = form.cleaned_data['año_max']
            precio_min = form.cleaned_data['precio_min']
            precio_max = form.cleaned_data['precio_max']

            if query:
                queryset = queryset.filter(
                    modelos__nombre__icontains=query
                ) | queryset.filter(
                    modelos__marca__marca__icontains=query
                )

            if marca:
                queryset = queryset.filter(modelos__marcas=marca)
                
            if categoria:
                queryset = queryset.filter(modelos__categoria=categoria)
                
            if km_min is not None:
                queryset = queryset.filter(km__gte=km_min)
                
            if km_max is not None:
                queryset = queryset.filter(km__lte=km_max)
                
            if año_min is not None:
                queryset = queryset.filter(modelos__año__gte=año_min)
                
            if año_max is not None:
                queryset = queryset.filter(modelos__año__lte=año_max)
                
            if precio_min is not None:
                queryset = queryset.filter(venta__gte=precio_min)
                
            if precio_max is not None:
                queryset = queryset.filter(venta__lte=precio_max)

        return queryset

class VehiculosListAdminView(ListView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculos_list_admin.html'
    context_object_name = 'vehiculos'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        form = VehiculoSearchForm(self.request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            marca = form.cleaned_data['marca']
            categoria = form.cleaned_data['categoria']
            km_min = form.cleaned_data['km_min']
            km_max = form.cleaned_data['km_max']
            año_min = form.cleaned_data['año_min']
            año_max = form.cleaned_data['año_max']
            precio_min = form.cleaned_data['precio_min']
            precio_max = form.cleaned_data['precio_max']

            if query:
                queryset = queryset.filter(
                    modelos__nombre__icontains=query
                ) | queryset.filter(
                    modelos__marca__marca__icontains=query
                )

            if marca:
                queryset = queryset.filter(modelos__marcas=marca)
                
            if categoria:
                queryset = queryset.filter(modelos__categoria=categoria)
                
            if km_min is not None:
                queryset = queryset.filter(km__gte=km_min)
                
            if km_max is not None:
                queryset = queryset.filter(km__lte=km_max)
                
            if año_min is not None:
                queryset = queryset.filter(modelos__año__gte=año_min)
                
            if año_max is not None:
                queryset = queryset.filter(modelos__año__lte=año_max)
                
            if precio_min is not None:
                queryset = queryset.filter(venta__gte=precio_min)
                
            if precio_max is not None:
                queryset = queryset.filter(venta__lte=precio_max)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VehiculoSearchForm(self.request.GET)
        context['background_image'] = staticfiles_storage.url('images/auto.avif')
        return context


class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculo_detalle.html'
    context_object_name = 'vehiculo'


class VehiculoCreateView(CreateView):
    model = Vehiculo
    form_class = VehiculoForm
    template_name = 'vehiculos/vehiculo_create.html'
    success_url = reverse_lazy('vehiculos_app:vehiculo-list')

class ModeloCreateView(CreateView):
    model = Modelos
    form_class = ModelosForm
    template_name = 'vehiculos/modelo_create.html'
    success_url = reverse_lazy('vehiculos_app:vehiculo-create')


class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'vehiculos/proveedor_create.html'
    fields = ['nombre', 'apellido', 'direccion', 'telefono', 'mail', 'paginaWeb', 'estado']
    success_url = reverse_lazy('vehiculos_app:vehiculo-create')

class CategoriaCreateView(CreateView):
    model = Categorias
    template_name = 'vehiculos/categoria_create.html'
    fields = ['tipoVehiculo']
    success_url = reverse_lazy('vehiculos_app:categoria-create')

class MarcaCreateView(CreateView):
    model = Marcas
    template_name = 'vehiculos/marca_create.html'
    fields = ['marca']
    success_url = reverse_lazy('vehiculos_app:marca-create')

class FichaTecnicaCreateView(CreateView):
    model = FichasTecnicas
    template_name = 'vehiculos/ficha_tecnica_create.html'
    fields = ['puertas', 'cilindradas', 'combustible', 'paisFabrica']
    success_url = reverse_lazy('vehiculos_app:ficha-tecnica-create')

class VehiculoDeleteView(DeleteView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculo_confirm_delete.html'
    success_url = reverse_lazy('vehiculos_app:vehiculo-list')