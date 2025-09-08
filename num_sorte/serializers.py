from rest_framework import serializers
from .models import LuckyNumber

class LuckyNumberSerializer(serializers.ModelSerializer):
    batch_series = serializers.SerializerMethodField()  

    class Meta:
        model = LuckyNumber
        fields = ['number', 'batch_series']  

    def get_batch_series(self, obj):
        control = obj.number_controls.first()
        if control:
            return {"batch": control.batch, "series": control.series}
        return None
