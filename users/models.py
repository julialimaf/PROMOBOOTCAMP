from django.db import models

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    cpf = models.CharField(max_length=11, unique=True)
    first_name = models.CharField("Nome", max_length=150)
    last_name = models.CharField("Sobrenome", max_length=150)
    email = models.EmailField("E-mail", unique=True)
    telefone = models.CharField("Telefone", max_length=20, blank=True)
    endereco_estado = models.CharField("Estado", max_length=50)
    endereco_cidade = models.CharField("Cidade", max_length=50)
    endereco_cep = models.CharField("CEP", max_length=10)

    USERNAME_FIELD = 'cpf'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    def __str__(self):
        return f"{self.cpf} - {self.first_name}"
