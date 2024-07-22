from django.db import models

class Produtos(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
