from django import forms

from .models import Unidade


class UnidadeModelForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = ['sigla', 'digitos']