from rest_framework import serializers
from .models import Faq, Regulations, PrivacyPolicy

class FaqSerializers(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'pergunta', 'resposta']


class RegulationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Regulations
        fields = ['id', 'conteudo']


class PrivacyPolicySerializers(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['id', 'conteudo']
