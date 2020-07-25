from django.urls import path

from unidade import views

urlpatterns = [
    path('list', views.list_unidades, name='list-unidades'),
    path('create', views.create_unidade, name='create-unidade'),
    path('update/<int:unidade_id>', views.update_unidade, name='update-unidade'),
    path('delete/<int:unidade_id>', views.delete_unidade, name='delete-unidade'),
]