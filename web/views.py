from django.shortcuts import render
from .models import Proyecto

def index(request):
    return render(request, 'Web/index.html')

def proyectos(request):
    proyectos = Proyecto.objects.all()
    return render(request, 'Web/projects/list.html', {'proyectos': proyectos})

def sobre_mi(request):
    return render(request, 'Web/sobre_mi.html')

def contacto(request):
    return render(request, 'Web/contacto.html')
