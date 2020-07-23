from django.db import models
from django.core.exceptions import ValidationError

def verifica_se_usuario_ja_existe(value):
    usuario = Usuario.objects.filter(nome__iexact=value)
    if usuario:
        raise ValidationError(
            f'O usuário {value} já existe',
            params={'value': value},
        )

class Usuario(models.Model):
    nome = models.CharField(
        max_length=50, verbose_name='Nome', validators=[verifica_se_usuario_ja_existe]
    )

    def __str__(self):
        return self.nome
