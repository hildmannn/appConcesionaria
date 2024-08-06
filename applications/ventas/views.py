from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Ventas
from .forms import VentasForm

class VentasListView(ListView):
    model = Ventas
    template_name = 'ventas/ventas_list.html'
    context_object_name = 'ventas'

class VentasDetailView(DetailView):
    model = Ventas
    template_name = 'ventas/ventas_detail.html'
    context_object_name = 'venta'

class VentasCreateView(CreateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'ventas/ventas_form.html'
    success_url = reverse_lazy('ventas:ventas_list')

class VentasUpdateView(UpdateView):
    model = Ventas
    form_class = VentasForm
    template_name = 'ventas/ventas_form.html'
    success_url = reverse_lazy('ventas:ventas_list')

class VentasDeleteView(DeleteView):
    model = Ventas
    template_name = 'ventas/ventas_confirm_delete.html'
    success_url = reverse_lazy('ventas:ventas_list')

