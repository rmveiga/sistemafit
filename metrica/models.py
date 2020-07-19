from django.db import models

from unidade.models import Unidade

class Metrica(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    unidade = models.ForeignKey(Unidade, on_delete=models.DO_NOTHING, verbose_name='Unidade')

    def __str__(self):
        return self.nome
