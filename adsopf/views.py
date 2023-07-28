from django.shortcuts import render
from django.http import HttpResponse
from .models import CompetenciaLaboral
from django.shortcuts import render # , get_object_or_404

# Create your views here.
def competencias(request):
    competencias = CompetenciaLaboral.objects.all()
    return render(request, 'index.html', {
        'competencias': competencias
    })

def lista_competencias(request):
    competencias = CompetenciaLaboral.objects.all()
    return render(request, 'index.html', {
        'competencias': competencias, 'menu': True
        })

def detalle_competencia(request, competencia_id):
    competencia = CompetenciaLaboral.objects.get(id=competencia_id)
    return render(request, 'detalles.html', {
        'competencia': competencia, 'menu': False
        })

def volver(request):
    return competencias
