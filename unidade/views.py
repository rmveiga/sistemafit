from django.shortcuts import render, redirect
from django.contrib import messages

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
        sigla_form = request.POST.get('sigla')
        unidade_filtro = Unidade.objects.filter(sigla__iexact=sigla_form)

        if unidade_filtro:
            messages.add_message(
                request, messages.WARNING,
                f'A unidade {sigla_form} já está cadastrada'
            )
            form = UnidadeModelForm(data=request.POST)
        else:
            form = UnidadeModelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Unidade cadastrada com sucesso'
                )

                return redirect('unidade:list-unidades')
    else:
        form = UnidadeModelForm()

    context = {
        'form': form,
    }

    return render(request, 'unidades/create.html', context=context)

def update_unidade(request, unidade_id):
    unidade_db = Unidade.objects.get(pk=unidade_id)

    if request.method == 'POST':
        sigla_form = request.POST.get('sigla')
        unidade_filtro = Unidade.objects.filter(sigla__iexact=sigla_form)

        if sigla_form != unidade_db.sigla and len(unidade_filtro) > 0:
            messages.add_message(
                request, messages.WARNING,
                f'A unidade {sigla_form} já está cadastrada'
            )
            form = UnidadeModelForm(data=request.POST)
        else:
            form = UnidadeModelForm(data=request.POST, instance=unidade_db)

            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Unidade alterada com sucesso'
                )

                return redirect('unidade:list-unidades')
    else:
        form = UnidadeModelForm(instance=unidade_db)

    context = {
        'form': form
    }

    return render(request, 'unidades/update.html', context=context)

def delete_unidade(request, unidade_id):
    unidade = Unidade.objects.get(pk=unidade_id)
    unidade.delete()
    messages.add_message(
        request, messages.SUCCESS,
        f'Unidade excluída com sucesso'
    )

    return redirect('unidade:list-unidades')