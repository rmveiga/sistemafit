from rest_framework import viewsets

from metrica.models import Metrica
from .serializers import MetricaSerializer

class MetricaViewset(viewsets.ModelViewSet):
    queryset = Metrica.objects.all()
    serializer_class = MetricaSerializer