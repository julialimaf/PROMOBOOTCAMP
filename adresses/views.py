from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Ceps, States, Cities
from .serializers import CepsSerializer, StatesSerializer, CitiesSerializer

class CepsViewSet(viewsets.ModelViewSet):
    queryset = Ceps.objects.all()
    serializer_class = CepsSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['city', 'state']  

class StatesViewSet(viewsets.ModelViewSet):
    queryset = States.objects.all()
    serializer_class = StatesSerializer


class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['state']  
