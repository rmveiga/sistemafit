from django.shortcuts import render

from .models import Acompanhamento

def listagem_acompanhamentos(request):
    acompanhamentos = Acompanhamento.objects.all()

    content = {
        'acompanhamentos': acompanhamentos
    }

    return render(request, 'acompanhamentos.html', content)
