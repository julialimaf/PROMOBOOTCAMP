from rest_framework import serializers
from .models import Faq, Regulamento, PoliticaPrivacidade

class FaqSerializers(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'pergunta', 'resposta']


class RegulamentoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Regulamento
        fields = ['id', 'conteudo']


class PoliticaPrivacidadeSerializers(serializers.ModelSerializer):
    class Meta:
        model = PoliticaPrivacidade
        fields = ['id', 'conteudo']
