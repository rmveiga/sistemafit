from django.urls import path
from rest_framework import routers

from usuario import views
from .api.viewsets import UsuarioViewset

usuario_router = routers.DefaultRouter()
usuario_router.register('usuarios', UsuarioViewset, basename='api-usuarios')

urlpatterns = [
    path('list', views.list_usuarios, name='list-usuarios'),
    path('create', views.create_usuario, name='create-usuario'),
    path('update/<int:usuario_id>', views.update_usuario, name='update-usuario'),
    path('delete/<int:usuario_id>', views.delete_usuario, name='delete-usuario'),
]