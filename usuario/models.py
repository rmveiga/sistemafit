from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return self.nome
