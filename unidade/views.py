from django.shortcuts import render

from .models import Unidade

def listagem_unidades(request):
    unidades = Unidade.objects.all()

    content = {
        'unidades': unidades
    }

    return render(request, 'unidades.html', content)
