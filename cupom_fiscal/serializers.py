from rest_framework import serializers
from .models import CupomFiscal

class CupomFiscalSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = CupomFiscal
        fields = ['id', 'usuario', 'titulo_produto', 'quantidade', 'data_cadastro']
        read_only_fields = ['usuario', 'data_cadastro']
