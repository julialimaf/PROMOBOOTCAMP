from django.db import models
from django.conf import settings
from django.utils import timezone   
from django.db import models
from users.models import CustomUser  

class CupomFiscal(models.Model):
    id = models.AutoField(primary_key=True)
    cnpj = models.CharField(max_length=18, default='00.000.000/0000-00')
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='cupons')
    imagem = models.ImageField(upload_to='midias/', default='default.jpg')
    titulo_produto = models.CharField(max_length=255)
    quantidade = models.PositiveIntegerField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo_produto} - {self.usuario.username}"