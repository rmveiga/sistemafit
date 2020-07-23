from django.urls import path

from usuario import views

urlpatterns = [
    path('list', views.list_usuarios, name='list'),
    path('create', views.create_usuario, name='create'),
    path('update/<int:usuario_id>', views.update_usuario, name='update'),
    path('delete/<int:usuario_id>', views.delete_usuario, name='delete'),
]