from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    altura = models.FloatField(verbose_name='Altura', blank=True, null=True)

    def __str__(self):
        return self.nome
