from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Acompanhamento
from .forms import AcompanhamentoModelForm

def list_acompanhamentos(request):
    acompanhamentos = Acompanhamento.objects.all()

    context = {
        'acompanhamentos': acompanhamentos
    }

    return render(request, 'acompanhamentos/list.html', context=context)

def create_acompanhamento(request):
    if request.method == 'POST':
        valido = True

        if valido:
            form = AcompanhamentoModelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Acompanhamento cadastrado com sucesso'
                )

                return redirect('acompanhamento:list-acompanhamentos')
        else:
            form = AcompanhamentoModelForm(data=request.POST)
    else:
        form = AcompanhamentoModelForm()

    context = {
        'form': form,
    }

    return render(request, 'acompanhamentos/create.html', context=context)

def update_acompanhamento(request, acompanhamento_id):
    acompanhamento = Acompanhamento.objects.get(pk=acompanhamento_id)

    if request.method == 'POST':
        valido = True

        if valido:
            form = AcompanhamentoModelForm(data=request.POST, instance=acompanhamento)

            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Acompanhamento alterado com sucesso'
                )

                return redirect('acompanhamento:list-acompanhamentos')
        else:
            form = AcompanhamentoModelForm(data=request.POST)
    else:
        form = AcompanhamentoModelForm(instance=acompanhamento)

    context = {
        'form': form
    }

    return render(request, 'acompanhamentos/update.html', context=context)