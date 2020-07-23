from django.shortcuts import render, redirect

from .models import Usuario
from .forms import UsuarioModelForm

def list_usuarios(request):
    usuarios = Usuario.objects.all()

    content = {
        'usuarios': usuarios
    }

    return render(request, 'usuarios/list.html', content)

def create_usuario(request):
    if request.method == 'POST':
        form = UsuarioModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios:list')
    else:
        form = UsuarioModelForm()

    context = {
        'form': form
    }

    return render(request, 'usuarios/create.html', context=context)

def update_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)

    if request.method == 'POST':
        form = UsuarioModelForm(data=request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario:list')
    else:
        form = UsuarioModelForm(instance=usuario)

    context = {
        'form': form
    }

    return render(request, 'usuarios/update.html', context=context)