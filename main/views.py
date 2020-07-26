from django.shortcuts import render
from django.contrib import messages

def home(request):
    messages.add_message(
        request, messages.INFO,
        f'Selecione um módulo para acessar os dados.'
    )
    return render(request, 'base.html')
