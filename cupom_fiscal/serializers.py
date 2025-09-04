from rest_framework import serializers
from .models import CupomFiscal
from num_sorte.models import NumeroSorte
from num_sorte.serializers import NumeroSorteSerializer    
class NumeroSorteSerializer(serializers.ModelSerializer):
    lote_serie = serializers.ReadOnlyField()

    class Meta:
        model = NumeroSorte
        fields = ['numero', 'lote_serie']

class CupomFiscalSerializer(serializers.ModelSerializer):
    numeros_sorte = serializers.SerializerMethodField()  

    class Meta:
        model = CupomFiscal
        fields = ['id', 'usuario', 'cnpj', 'imagem', 'titulo_produto', 'quantidade', 'data_cadastro', 'numeros_sorte']
        read_only_fields = ['usuario', 'data_cadastro', 'numeros_sorte']

    def get_numeros_sorte(self, obj):
        numeros = NumeroSorte.objects.filter(cupom_fiscal_id=obj.id)
        return NumeroSorteSerializer(numeros, many=True).data