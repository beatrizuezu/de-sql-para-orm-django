from django.db import models
from categoria.models import Categoria


class Produto(models.Model):
    nome = models.CharField(u'Nome', max_length=128)
    valor = models.DecimalField(u'Valor', max_digits=10, decimal_places=2, blank=True, null=True)
    categoria = models.ForeignKey('Categoria')
