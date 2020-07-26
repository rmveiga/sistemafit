from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Metrica
from .forms import MetricaModelForm

def verifica_se_metrica_ja_existe(request, metrica=None):
    nome = request.POST.get('nome')
    metricas = Metrica.objects.filter(nome__iexact=nome)

    if metrica is None:
        if metricas:
            return False
    elif nome != metrica.nome and metricas:
            return False
    return True

def list_metricas(request):
    metricas = Metrica.objects.all()

    context = {
        'metricas': metricas
    }

    return render(request, 'metricas/list.html', context=context)

def create_metrica(request):
    if request.method == 'POST':
        valido = True
        if not verifica_se_metrica_ja_existe(request):
            valido = False
            messages.add_message(
                request, messages.WARNING,
                f'A métrica {request.POST.get("nome")} já está cadastrada'
            )

        if valido:
            form = MetricaModelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Métrica cadastrada com sucesso'
                )

                return redirect('metrica:list-metricas')
        else:
            form = MetricaModelForm(data=request.POST)
    else:
        form = MetricaModelForm()

    context = {
        'form': form,
    }

    return render(request, 'metricas/create.html', context=context)

def update_metrica(request, metrica_id):
    metrica = Metrica.objects.get(pk=metrica_id)

    if request.method == 'POST':
        valido = True
        if not verifica_se_metrica_ja_existe(request, metrica):
            valido = False
            messages.add_message(
                request, messages.WARNING,
                f'A métrica {request.POST.get("nome")} já está cadastrada'
            )

        if valido:
            form = MetricaModelForm(data=request.POST, instance=metrica)

            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Métrica alterada com sucesso'
                )

                return redirect('metrica:list-metricas')
        else:
            form = MetricaModelForm(data=request.POST)
    else:
        form = MetricaModelForm(instance=metrica)

    context = {
        'form': form
    }

    return render(request, 'metricas/update.html', context=context)

def delete_metrica(request, metrica_id):
    metrica = Metrica.objects.get(pk=metrica_id)
    metrica.delete()
    messages.add_message(
        request, messages.SUCCESS,
        f'Métrica excluída com sucesso'
    )

    return redirect('metrica:list-metricas')