from rest_framework import serializers
from .models import NumeroSorte

class NumeroSorteSerializer(serializers.ModelSerializer):
    lote_serie = serializers.ReadOnlyField()

    class Meta:
        model = NumeroSorte
        fields = ['id', 'numero', 'lote_serie']
