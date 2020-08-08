from rest_framework import serializers

from acompanhamento.models import Acompanhamento

class AcompanhamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acompanhamento
        fields = (
            'id', 'dt_medicao', 'medida', 'metrica', 'usuario',
        )