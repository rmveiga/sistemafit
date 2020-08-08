from django.urls import path
from rest_framework import routers

from acompanhamento import views
from .api.viewsets import AcompanhamentoViewset

acompanhamento_router = routers.DefaultRouter()
acompanhamento_router.register('acompanhamentos', AcompanhamentoViewset, basename='api-acompanhamentos')

urlpatterns = [
    path('list', views.list_acompanhamentos, name='list-acompanhamentos'),
    path('create', views.create_acompanhamento, name='create-acompanhamento'),
    path('update/<int:acompanhamento_id>', views.update_acompanhamento, name='update-acompanhamento'),
    path('delete/<int:acompanhamento_id>', views.delete_acompanhamento, name='delete-acompanhamento'),
]