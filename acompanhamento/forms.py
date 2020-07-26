from django import forms

from .models import Acompanhamento


class AcompanhamentoModelForm(forms.ModelForm):
    class Meta:
        model = Acompanhamento
        fields = [
            'dt_medicao', 'medida', 'metrica', 'usuario'
        ]