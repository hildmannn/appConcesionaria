from django.shortcuts import render
from django.templatetags.static import static
# Create your views here.



def home_view(request):
    context = {
        'background_image': static('images/fondo.jpeg'),
    }
    return render(request, 'home/home.html', context)
