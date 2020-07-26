from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Metrica
from .forms import MetricaModelForm

def list_metricas(request):
    metricas = Metrica.objects.all()

    content = {
        'metricas': metricas
    }

    return render(request, 'metricas/list.html', content)

def create_metrica(request):
    if request.method == 'POST':
        valido = True

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