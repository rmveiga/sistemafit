from django.shortcuts import render, redirect

from .models import Unidade
from .forms import UnidadeModelForm

def list_unidades(request):
    unidades = Unidade.objects.all()

    content = {
        'unidades': unidades
    }

    return render(request, 'unidades/list.html', content)

def create_unidade(request):
    if request.method == 'POST':
        form = UnidadeModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('unidade:list-unidades')
    else:
        form = UnidadeModelForm()

    context = {
        'form': form
    }

    return render(request, 'unidades/create.html', context=context)
