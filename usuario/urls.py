from django.urls import path

from usuario import views

urlpatterns = [
    path('list', views.list_usuarios, name='list'),
    path('create', views.create_usuario, name='create'),
]