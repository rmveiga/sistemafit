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

from . import views
from unidade.urls import unidade_router
from metrica.urls import metrica_router
from usuario.urls import usuario_router
from acompanhamento.urls import acompanhamento_router

urlpatterns = [
    path('admin/', admin.site.urls),
    # System Paths
    path('', views.home),
    path('acompanhamentos/', include(('acompanhamento.urls', 'acompanhamento'), namespace='acompanhamento')),
    path('usuarios/', include(('usuario.urls', 'usuario'), namespace='usuario')),
    path('unidades/', include(('unidade.urls', 'unidade'), namespace='unidade')),
    path('metricas/', include(('metrica.urls', 'metrica'), namespace='metrica')),
    # API Routes
    path('api/', include(unidade_router.urls )),
    path('api/', include(metrica_router.urls )),
    path('api/', include(usuario_router.urls )),
    path('api/', include(acompanhamento_router.urls )),
]
