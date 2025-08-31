from django.db import models


class Faq(models.Model):
    pergunta = models.CharField(max_length=255)
    resposta = models.TextField()

    def __str__(self):
        return self.pergunta


class Regulamento(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Regulamento"


class PoliticaPrivacidade(models.Model):
    conteudo = models.TextField()

    def __str__(self):
        return "Política de Privacidade"
