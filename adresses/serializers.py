
from .models import Ceps, States, Cities
from rest_framework import generics
from rest_framework import serializers
from .models import Ceps, States, Cities

class CepsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ceps
        fields = '__all__'


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'
