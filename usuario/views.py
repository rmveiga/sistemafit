from django.shortcuts import render

from .models import Usuario

def listagem_usuarios(request):
    usuarios = Usuario.objects.all()

    content = {
        'usuarios': usuarios
    }

    return render(request, 'usuarios.html', content)
