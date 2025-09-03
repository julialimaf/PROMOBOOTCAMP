from django.db import models
from users.models import CustomUser
from cupom_fiscal.models import CupomFiscal
from django.utils import timezone
class ControleNumeroSorte(models.Model):
    
    
    lote = models.IntegerField("Lote")
    serie = models.IntegerField("Série")
    max_serie = models.IntegerField("Máxima Série")
    numero = models.ForeignKey('NumeroSorte', on_delete=models.CASCADE, related_name='controle_numeros')  


    def __str__(self):
        return f"Número: {self.numero} - Lote: {self.lote} - Série: {self.serie}"
    
class NumeroSorte(models.Model):
    numero = models.IntegerField("Número da Sorte", unique=True)
    usuario = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='numeros_sorte')
    cupom_fiscal = models.ForeignKey('cupom_fiscal.CupomFiscal', on_delete=models.CASCADE, related_name='numeros_sorte')
    criado_em = models.DateTimeField("Criado em", default=timezone.now)

    def __str__(self):
        return f"Número: {self.numero} - Usuário: {self.usuario.cpf} - Cupom: {self.cupom_fiscal.id_cupom}"