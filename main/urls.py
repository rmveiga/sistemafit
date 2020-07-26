"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from acompanhamento.views import (
    listagem_acompanhamentos
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listagem_acompanhamentos),
    path('usuarios/', include(('usuario.urls', 'usuario'), namespace='usuario')),
    path('unidades/', include(('unidade.urls', 'unidade'), namespace='unidade')),
    path('metricas/', include(('metrica.urls', 'metrica'), namespace='metrica')),
    path('acompanhamentos/', listagem_acompanhamentos),
]
