from django.shortcuts import render

from .models import Unidade

def list_unidades(request):
    unidades = Unidade.objects.all()

    content = {
        'unidades': unidades
    }

    return render(request, 'unidades/list.html', content)
