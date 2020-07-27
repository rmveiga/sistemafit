from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime

from .models import Acompanhamento
from .forms import AcompanhamentoModelForm

def verifica_se_data_medicao_eh_futura(request):
    dt_medicao = datetime.strptime(request.POST.get('dt_medicao'), '%Y-%m-%d').date()
    hoje = datetime.now().date()

    if dt_medicao > hoje:
        return False
    return True

def verifica_se_medida_negativo(request):
    medida = float(request.POST.get('medida'))
    if medida < 0:
        return False
    return True

def list_acompanhamentos(request):
    acompanhamentos = Acompanhamento.objects.all()
    if not acompanhamentos:
        messages.add_message(
            request, messages.INFO,
            f'Cadastre o primeiro acompanhamento'
        )

    context = {
        'acompanhamentos': acompanhamentos
    }

    return render(request, 'acompanhamentos/list.html', context=context)

def create_acompanhamento(request):
    if request.method == 'POST':
        valido = True
        if not verifica_se_data_medicao_eh_futura(request):
            valido = False
            messages.add_message(
                request, messages.WARNING,
                f'A data de medição não pode ser posterior ao dia de hoje'
            )
        if not verifica_se_medida_negativo(request):
            valido = False
            messages.add_message(
                request, messages.WARNING,
                f'O valor da medida não pode ser negativo'
            )

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
        if not verifica_se_data_medicao_eh_futura(request):
            valido = False
            messages.add_message(
                request, messages.WARNING,
                f'A data de medição não pode ser posterior ao dia de hoje'
            )
        if not verifica_se_medida_negativo(request):
            valido = False
            messages.add_message(
                request, messages.WARNING,
                f'O valor da medida não pode ser negativo'
            )

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

def delete_acompanhamento(request, acompanhamento_id):
    acompanhamento = Acompanhamento.objects.get(pk=acompanhamento_id)
    acompanhamento.delete()
    messages.add_message(
        request, messages.SUCCESS,
        f'Acompanhamento excluído com sucesso'
    )

    return redirect('acompanhamento:list-acompanhamentos')