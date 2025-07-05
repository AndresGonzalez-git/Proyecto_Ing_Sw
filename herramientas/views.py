from django.shortcuts import render, get_object_or_404
from .models import HerramientaIA

# Create your views here.

def ficha_herramienta(request, id):
    herramienta = get_object_or_404(HerramientaIA, id=id)
    return render(request, 'ficha_herramienta.html', {'herramienta': herramienta})

def lista_herramientas(request):
    herramientas = HerramientaIA.objects.all()
    return render(request, 'herramientas/lista_herramientas.html', {'herramientas': herramientas})
