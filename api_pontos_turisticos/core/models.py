from django.db import models
from atracoes.models import Atracao


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    atracao = models.ManyToManyField(Atracao)
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
# Create your models here.
