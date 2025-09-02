from django.db import models
from django.conf import settings
from django.utils import timezone   
from django.db import models
from users.models import CustomUser  

class CupomFiscal(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cupons')
    
    titulo_produto = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo_produto} - {self.usuario.username}"