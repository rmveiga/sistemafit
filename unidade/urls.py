from django.urls import path

from unidade import views

urlpatterns = [
    path('list', views.list_unidades, name='list-unidade'),
    # path('create', views.create_usuario, name='create'),
    # path('update/<int:usuario_id>', views.update_usuario, name='update'),
    # path('delete/<int:usuario_id>', views.delete_usuario, name='delete'),
]