from django.templatetags.static import static
from django.views.generic import ListView
from applications.vehiculos.models import Vehiculo
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm, LoginForm
from django.db import IntegrityError
from .models import Usuarios
# Vista para listar vehículos
class VehiculosListView(ListView):
    model = Vehiculo
    template_name = 'home/vehiculos_list.html'
    context_object_name = 'vehiculos'
    paginate_by = 10

# Vista de inicio
def home_view(request):
    if request.user.is_authenticated:
        # Redirección según el rol del usuario
        if request.user.role == 'admin':
            return redirect('home_app:admin_dashboard')
        elif request.user.role == 'empleado':
            return redirect('home_app:empleado_dashboard')
        else:
            return redirect('home_app:usuario_dashboard')
    else:
        # Si el usuario no está autenticado, renderiza la página de inicio
        context = {'background_image': static('images/fondo.jpeg')}
        return render(request, 'home/home.html', context)

# Vistas de dashboard según el rol
def admin_dashboard(request):
    return render(request, 'home/admin_dashboard.html')

def empleado_dashboard(request):
    return render(request, 'home/empleado_dashboard.html')

def usuario_dashboard(request):
    return render(request, 'home/usuario_dashboard.html')

# Vista de registro

def register_view(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_app:login')
        else:
            return render(request, "home/register.html", {"form": form})
    else:
        form = RegistroForm()
    return render(request, "home/register.html", {"form": form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home_app:home')
            else:
                form.add_error(None, 'Credenciales inválidas.')
    else:
        form = LoginForm()
    return render(request, 'home/login.html', {'form': form})
