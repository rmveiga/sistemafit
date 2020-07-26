from django import forms

from .models import Metrica


class MetricaModelForm(forms.ModelForm):
    class Meta:
        model = Metrica
        fields = ['nome', 'unidade']