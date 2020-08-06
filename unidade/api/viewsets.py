from rest_framework import viewsets

from unidade.models import Unidade
from .serializers import UnidadeSerializer

class UnidadeViewset(viewsets.ModelViewSet):
    queryset = Unidade.objects.all()
    serializer_class = UnidadeSerializer