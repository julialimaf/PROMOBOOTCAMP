from rest_framework import serializers
from .models import LuckyNumber

class LuckyNumberSerializer(serializers.ModelSerializer):
    batch_series = serializers.ReadOnlyField()

    class Meta:
        model = LuckyNumber
        fields = ['id', 'number', 'batch_series']
