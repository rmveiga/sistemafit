from django.urls import path

from usuario import views

urlpatterns = [
    path('list', views.list_usuarios, name='list-usuarios'),
    path('create', views.create_usuario, name='create-usuario'),
    path('update/<int:usuario_id>', views.update_usuario, name='update-usuario'),
    path('delete/<int:usuario_id>', views.delete_usuario, name='delete-usuario'),
]