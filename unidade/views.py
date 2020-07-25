from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Unidade
from .forms import UnidadeModelForm

def verifica_se_unidade_ja_existe(request, unidade=None):
    sigla = request.POST.get('sigla')
    unidades = Unidade.objects.filter(sigla__iexact=sigla)

    if unidade is None:
        if unidades:
            return False
    elif sigla != unidade.sigla and unidades:
            return False
    return True

def verifica_se_digito_negativo(request):
    digito = int(request.POST.get('digitos'))
    if digito < 0:
        return False
    return True

def list_unidades(request):
    unidades = Unidade.objects.all()

    content = {
        'unidades': unidades
    }

    return render(request, 'unidades/list.html', content)

def create_unidade(request):
    if request.method == 'POST':
        valido = True
        if not verifica_se_unidade_ja_existe(request):
            valido = False
            form = UnidadeModelForm(data=request.POST)
            messages.add_message(
                request, messages.WARNING,
                f'A unidade {request.POST.get("sigla")} já está cadastrada'
            )
        if not verifica_se_digito_negativo(request):
            valido = False
            form = UnidadeModelForm(data=request.POST)
            messages.add_message(
                request, messages.WARNING,
                'A quantidade de dígitos não pode ser negativa'
            )

        if valido:
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
    unidade = Unidade.objects.get(pk=unidade_id)

    if request.method == 'POST':
        valido = True
        if not verifica_se_unidade_ja_existe(request, unidade):
            valido = False
            form = UnidadeModelForm(data=request.POST)
            messages.add_message(
                request, messages.WARNING,
                f'A unidade {request.POST.get("sigla")} já está cadastrada'
            )
        if not verifica_se_digito_negativo(request):
            valido = False
            form = UnidadeModelForm(data=request.POST)
            messages.add_message(
                request, messages.WARNING,
                'A quantidade de dígitos não pode ser negativa'
            )

        if valido:
            form = UnidadeModelForm(data=request.POST, instance=unidade)

            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Unidade alterada com sucesso'
                )

                return redirect('unidade:list-unidades')
    else:
        form = UnidadeModelForm(instance=unidade)

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