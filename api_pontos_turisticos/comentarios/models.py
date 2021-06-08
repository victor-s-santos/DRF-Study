from django.contrib.auth.models import User
from django.db import models

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delelte=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'

    def __str__(self):
        return self.usuario.first_name

# Create your models here.
