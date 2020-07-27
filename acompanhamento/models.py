from django.db import models
from django.utils import timezone

from usuario.models import Usuario
from metrica.models import Metrica

class Acompanhamento(models.Model):
    dt_medicao = models.DateField(verbose_name='Data de Medição', default=timezone.now().date())
    medida = models.FloatField(verbose_name='Medida')
    metrica = models.ForeignKey(Metrica, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{str(self.dt_medicao)} - {self.metrica}'

