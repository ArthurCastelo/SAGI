from django.db import models
from django.contrib.auth.models import User


class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

