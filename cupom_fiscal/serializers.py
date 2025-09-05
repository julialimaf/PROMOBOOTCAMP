from rest_framework import serializers
from .models import FiscalCoupon
from num_sorte.models import LuckyNumber 
from num_sorte.serializers import LuckyNumberSerializer    
class LuckyNumberSerializer(serializers.ModelSerializer):
    lote_serie = serializers.ReadOnlyField()

    class Meta:
        model = LuckyNumber
        fields = ['numero', 'lote_serie']

class FiscalCouponSerializer(serializers.ModelSerializer):
    lucky_number = serializers.SerializerMethodField()  

    class Meta:
        model = FiscalCoupon
        fields = ['id', 'user_fk', 'cnpj', 'image', 'product_name', 'quantity', 'date_register', 'lucky_number']
        read_only_fields = ['user_fk', 'date_register', 'lucky_number']

    def get_lucky_number(self, obj):
        numbers = LuckyNumber.objects.filter(fiscal_coupon_id=obj.id)
        return LuckyNumberSerializer(numbers, many=True).data