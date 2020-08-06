from rest_framework import serializers

from metrica.models import Metrica

class MetricaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metrica
        fields = (
            'id', 'nome', 'unidade'
        )