from django.urls import path

from metrica import views

urlpatterns = [
    path('list', views.list_metricas, name='list-metricas'),
    path('create', views.create_metrica, name='create-metrica'),
    path('update/<int:metrica_id>', views.update_metrica, name='update-metrica'),
    path('delete/<int:metrica_id>', views.delete_metrica, name='delete-metrica'),
]