from django.db import models

class Categoria(models.Model):
    nome = models.CharField('Nome', max_length=128)

    def __str__(self):
        return '%s' % self.nome
