from django import forms

from .models import Usuario

class UsuarioModelForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nome', 'altura']