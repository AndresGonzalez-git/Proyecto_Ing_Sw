from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import HerramientaIA, CATEGORIAS_IA, NIVELES_EDUCATIVOS

# Create your views here.

def ficha_herramienta(request, id):
    herramienta = get_object_or_404(HerramientaIA, id=id)
    return render(request, 'ficha_herramienta.html', {'herramienta': herramienta})

def lista_herramientas(request):
    categorias_seleccionadas = request.GET.getlist('categoria')
    niveles_seleccionados = request.GET.getlist('nivel_educativo')
    
    herramientas_qs = HerramientaIA.objects.all()
    
    if categorias_seleccionadas:
        herramientas_qs = herramientas_qs.filter(categoria__in=categorias_seleccionadas)
    
    if niveles_seleccionados:
        herramientas_qs = herramientas_qs.filter(nivel_educativo__in=niveles_seleccionados)
    
    paginator = Paginator(herramientas_qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'herramientas/lista_herramientas.html', {
        'herramientas': page_obj,
        'categorias_disponibles': CATEGORIAS_IA,
        'categorias_seleccionadas': categorias_seleccionadas,
        'niveles_disponibles': NIVELES_EDUCATIVOS,
        'niveles_seleccionados': niveles_seleccionados,
        'page_obj': page_obj,
        'paginator': paginator,
    })

def aviso_privacidad(request):
    return render(request, 'herramientas/aviso_privacidad.html')

