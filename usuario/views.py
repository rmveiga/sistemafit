from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Usuario
from .forms import UsuarioModelForm

def verifica_se_usuario_ja_existe(request, usuario=None):
    nome = request.POST.get('nome')
    usuarios = Usuario.objects.filter(nome__iexact=nome)

    if usuario is None:
        if usuarios:
            return False
    elif nome != usuario.nome and usuarios:
            return False
    return True

def list_usuarios(request):
    usuarios = Usuario.objects.all()
    if not usuarios:
        messages.add_message(
            request, messages.INFO,
            f'Cadastre o primeiro usuário'
        )

    context = {
        'usuarios': usuarios
    }

    return render(request, 'usuarios/list.html', context=context)

def create_usuario(request):
    if request.method == 'POST':
        valido = True
        if not verifica_se_usuario_ja_existe(request):
            valido = False
            messages.add_message(
                request, messages.WARNING,
                f'O usuário {request.POST.get("nome")} já está cadastrado'
            )

        if valido:
            form = UsuarioModelForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Usuário cadastrado com sucesso'
                )
                return redirect('usuario:list-usuarios')
        else:
            form = UsuarioModelForm(data=request.POST)
    else:
        form = UsuarioModelForm()

    context = {
        'form': form
    }

    return render(request, 'usuarios/create.html', context=context)

def update_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)

    if request.method == 'POST':
        valido = True
        if not verifica_se_usuario_ja_existe(request):
            valido = False
            messages.add_message(
                request, messages.WARNING,
                f'O usuário {request.POST.get("nome")} já está cadastrado'
            )

        if valido:
            form = UsuarioModelForm(data=request.POST, instance=usuario)
            if form.is_valid():
                form.save()
                messages.add_message(
                    request, messages.SUCCESS,
                    f'Usuário alterado com sucesso'
                )
                return redirect('usuario:list-usuarios')
        else:
            form = UsuarioModelForm(data=request.POST)
    else:
        form = UsuarioModelForm(instance=usuario)

    context = {
        'form': form
    }

    return render(request, 'usuarios/update.html', context=context)

def delete_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    usuario.delete()
    messages.add_message(
        request, messages.SUCCESS,
        f'Usuário excluído com sucesso'
    )

    return redirect('usuario:list-usuarios')