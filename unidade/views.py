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
        'form': form,
    }

    return render(request, 'unidades/create.html', context=context)

def update_unidade(request, unidade_id):
    unidade = Unidade.objects.get(pk=unidade_id)

    if request.method == 'POST':
        if request.POST.get('sigla') != unidade.sigla:
            print('diferente')

        form = UnidadeModelForm(data=request.POST, instance=unidade)
        if form.is_valid():
            form.save()
            return redirect('unidade:list-unidades')
    else:
        form = UnidadeModelForm(instance=unidade)

    context = {
        'form': form
    }

    return render(request, 'unidades/update.html', context=context)