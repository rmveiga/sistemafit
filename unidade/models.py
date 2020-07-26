from django.db import models

class Unidade(models.Model):
    sigla = models.CharField(max_length=5, verbose_name='Sigla')
    digitos = models.IntegerField(verbose_name='Dígitos', default=0)

    def __str__(self):
        return self.sigla
