from django.shortcuts import render

from .models import Acompanhamento

def listagem_acompanhamentos(request):
    acompanhamento = Acompanhamento.objects.all()

    content = {
        'acompanhamento': acompanhamento
    }

    return render(request, 'acompanhamentos.html', content)
