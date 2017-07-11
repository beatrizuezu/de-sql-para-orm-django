from django.db import models

class Categoria(models.Model):
    nome = models.CharField(u'Nome', max_length=128) 
