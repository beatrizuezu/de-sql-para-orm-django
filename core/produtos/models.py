from django.db import models
from core.categorias.models import Categoria

class Produto(models.Model):
    nome = models.CharField(
        'Nome',
        max_length=128
    )
    valor = models.DecimalField(
        'Valor',
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    categoria = models.ForeignKey(Categoria, models.SET_NULL, null=True)

    def __str__(self):
        return '%s' % self.nome
