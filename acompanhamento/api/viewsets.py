from rest_framework import viewsets

from acompanhamento.models import Acompanhamento
from .serializers import AcompanhamentoSerializer

class AcompanhamentoViewset(viewsets.ModelViewSet):
    queryset = Acompanhamento.objects.all()
    serializer_class = AcompanhamentoSerializer