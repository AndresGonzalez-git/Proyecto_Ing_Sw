from django.shortcuts import render
from .models import InteligenciaArtificial

def busqueda(request):
    consulta = request.GET.get('q', '')
    resultados = []

    if consulta:
        resultados = InteligenciaArtificial.objects.filter(nombre__icontains=consulta)

    return render(request, 'ia/busqueda.html', {
        'consulta': consulta,
        'resultados': resultados
    })
