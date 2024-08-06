from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Vehiculo
from .forms import VehiculoSearchForm

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = VehiculoSearchForm(self.request.GET)
        return context


class VehiculoDetailView(DetailView):
    model = Vehiculo
    template_name = 'vehiculos/vehiculo_detalle.html'
    context_object_name = 'vehiculo'



