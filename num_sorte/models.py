from django.db import models

class NumeroSorte(models.Model):
    numero = models.IntegerField("Número da Sorte", unique=True)
    criado_em = models.DateTimeField("Criado em", auto_now_add=True)
