from django.shortcuts import render
from .models import InteligenciaArtificial
from django.http import HttpResponse 





# esta funcion renderiza la plantilla base.html
def base(request):
    return render(request, 'ia/base.html')

def busqueda(request):
    consulta = request.GET.get('q', '')
    resultados = []

    if consulta:
        resultados = InteligenciaArtificial.objects.filter(nombre__icontains=consulta)

    return render(request, 'ia/busqueda.html', {
        'consulta': consulta,
        'resultados': resultados
    })

def inicio(request):
    return render(request, 'ia/inicio.html')

def imagenes(request):
    return render(request, 'ia/categorias/imagenes.html')

def mapas_mentales(request):
    return render(request, 'ia/categorias/mapas_mentales.html')

def matematicas(request):
   
   return render(request, 'ia/categorias/matematicas.html')

def ppt(request):
    return render(request, 'ia/categorias/ppt.html')

def programacion(request):

    return render(request, 'ia/categorias/programacion.html')

def texto(request):
    
    return render(request, 'ia/categorias/texto.html')