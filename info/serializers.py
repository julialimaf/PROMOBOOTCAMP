from rest_framework import serializers
from .models import Faq, Regulations, PrivacyPolicy
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator



class FaqSerializers(serializers.ModelSerializer):

    
    class Meta:
        model = Faq
        fields = ['id', 'question', 'answer']


class RegulationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Regulations
        fields = ['id', 'content', 'file']


class PrivacyPolicySerializers(serializers.ModelSerializer):
    class Meta:
        model = PrivacyPolicy
        fields = ['id', 'content', 'file']
