from django.shortcuts import render
from rest_framework import generics
from .models import Faq, Regulamento, PoliticaPrivacidade
from .serializers import FaqSerializers, RegulamentoSerializers, PoliticaPrivacidadeSerializers


class FaqListView(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializers


class RegulamentoView(generics.RetrieveAPIView):
    queryset = Regulamento.objects.all()
    serializer_class = RegulamentoSerializers

    def get_object(self):
        return Regulamento.objects.last()

class PoliticaPrivacidadeView(generics.RetrieveAPIView):
    queryset = PoliticaPrivacidade.objects.all()
    serializer_class = PoliticaPrivacidadeSerializers

    def get_object(self):
        return PoliticaPrivacidade.objects.last()
