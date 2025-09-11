from django.shortcuts import render
from rest_framework import generics
from .models import Faq, Regulations, PrivacyPolicy
from .serializers import FaqSerializers, RegulationsSerializers, PrivacyPolicySerializers
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator


class FaqListView(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializers


    @method_decorator(cache_page(60*15))  
    def list(self, request, *args, **kwargs):
      print("eNTROU")
      return super().list(request, *args, **kwargs)

class RegulationsView(generics.RetrieveAPIView):
    queryset = Regulations.objects.all()
    serializer_class = RegulationsSerializers

    def get_object(self):
        return Regulations.objects.last()

class PrivacyPolicyView(generics.RetrieveAPIView):
    queryset = PrivacyPolicy.objects.all()
    serializer_class = PrivacyPolicySerializers

    def get_object(self):
        return PrivacyPolicy.objects.last()
