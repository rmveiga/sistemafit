from rest_framework import viewsets

from usuario.models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer