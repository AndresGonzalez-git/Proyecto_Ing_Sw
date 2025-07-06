from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import HerramientaIA, CATEGORIAS_IA, NIVELES_EDUCATIVOS

# Create your views here.

def ficha_herramienta(request, id):
    herramienta = get_object_or_404(HerramientaIA, id=id)
    return render(request, 'ficha_herramienta.html', {'herramienta': herramienta})

def lista_herramientas(request):
    categorias_seleccionadas = request.GET.getlist('categoria')
    if categorias_seleccionadas:
        herramientas_qs = HerramientaIA.objects.filter(categoria__in=categorias_seleccionadas)
    else:
        herramientas_qs = HerramientaIA.objects.all()
    paginator = Paginator(herramientas_qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'herramientas/lista_herramientas.html', {
        'herramientas': page_obj,
        'categorias_disponibles': CATEGORIAS_IA,
        'categorias_seleccionadas': categorias_seleccionadas,
        'page_obj': page_obj,
        'paginator': paginator,
    })

def lista_herramientas2(request):
    categorias_seleccionadas2 = request.GET.getlist('nivel_educativo')
    if categorias_seleccionadas2:
        herramientas_qs = HerramientaIA.objects.filter(categoria2__in=categorias_seleccionadas2)
    else:
        herramientas_qs = HerramientaIA.objects.all()
    paginator = Paginator(herramientas_qs, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'herramientas/lista_herramientas.html', {
        'herramientas2': page_obj,
        'categorias_disponibles2': NIVELES_EDUCATIVOS,
        'categorias_seleccionadas2': categorias_seleccionadas2,
        'page_obj2': page_obj,
        'paginator2': paginator,
    })




def aviso_privacidad(request):
    return render(request, 'herramientas/aviso_privacidad.html')

