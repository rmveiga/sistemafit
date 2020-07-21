from django.shortcuts import render

from .models import Metrica

def listagem_metricas(request):
    metricas = Metrica.objects.all()

    content = {
        'metricas': metricas
    }

    return render(request, 'metricas.html', content)
