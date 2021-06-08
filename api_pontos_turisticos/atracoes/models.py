from django.db import models

class Atracao(models.Model):
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    horario_func = models.TextField()
    idade_minima = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Recurso'
        verbose_name_plural = 'Recursos'
# Create your models here.
