from django.shortcuts import render

# Create your views here.
# home/views.py
from django.shortcuts import render

def home_view(request):
    return render(request, 'home/home.html')