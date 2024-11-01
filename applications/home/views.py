from django.shortcuts import render
from django.templatetags.static import static
from django.views.generic import ListView
from applications.vehiculos.models import Vehiculo
# Create your views here.

class VehiculosListView(ListView):
    model = Vehiculo
    template_name = 'home/vehiculos_list.html'
    context_object_name = 'vehiculos'
    paginate_by = 10


def home_view(request):
    context = {
        'background_image': static('images/fondo.jpeg'),
    }
    return render(request, 'home/home.html', context)


def nosotros(request):
    context = {
        'background_image': static('images/nosotros.jpeg'),
    }
    return render(request, 'home/nosotros.html', context)

