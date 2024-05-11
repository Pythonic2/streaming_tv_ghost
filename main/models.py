from django.db import models
from time import strftime
from django.utils.timezone import now


class Cliente(models.Model):
    email = models.EmailField(unique=True)
    usuario = models.CharField(max_length=100, default='temp')
    vencimento = models.DateField(default=now)

    def __str__(self) -> str:
        return self.usuario