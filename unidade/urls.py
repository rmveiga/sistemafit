from django.urls import path
from rest_framework import routers

from unidade import views
from .api.viewsets import UnidadeViewset

unidade_router = routers.DefaultRouter()
unidade_router.register('unidades', UnidadeViewset, basename='api-unidades')

urlpatterns = [
    path('list', views.list_unidades, name='list-unidades'),
    path('create', views.create_unidade, name='create-unidade'),
    path('update/<int:unidade_id>', views.update_unidade, name='update-unidade'),
    path('delete/<int:unidade_id>', views.delete_unidade, name='delete-unidade'),
]