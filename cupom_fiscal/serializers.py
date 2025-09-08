from rest_framework import serializers
from .models import FiscalCoupon, Pivo, Product
from num_sorte.models import LuckyNumber
from num_sorte.serializers import LuckyNumberSerializer



from rest_framework import serializers
class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [ "product_name"]

class LuckyNumberOnlySerializer(serializers.ModelSerializer):
    formatted_number = serializers.SerializerMethodField()  

    class Meta:
        model = LuckyNumber
        fields = ['formatted_number']
    def get_formatted_number(self, obj):
        num_str = str(obj.number)
        if len(num_str) <= 2:
            return num_str        #### ate agora ta dando certo, mas to com medo de não retornar as casas desejadas, infelizmente ####
        return f"{num_str[:2]}.{num_str[2:]}" 


class FiscalCouponSerializer(serializers.ModelSerializer):
    lucky_number = serializers.SerializerMethodField()
    product_name = serializers.CharField(write_only=True)
    quantity = serializers.IntegerField(write_only=True)

    class Meta:
        model = FiscalCoupon
        fields = ['id', 'cnpj', 'image', 'date_register', 'lucky_number', 'product_name', 'quantity']
        read_only_fields = ['date_register', 'lucky_number']

    def create(self, validated_data):
        product_name = validated_data.pop('product_name')
        quantity = validated_data.pop('quantity')
        validated_data.pop('user_fk', None) 
        user = self.context['request'].user

        coupon = FiscalCoupon.objects.create(user_fk=user, **validated_data)

        
        product, _ = Product.objects.get_or_create(product_name=product_name)
        Pivo.objects.create(coupon=coupon, product_name=product, quantity=quantity)

       
        from num_sorte.utils import generate_numbers_for_coupon
        generate_numbers_for_coupon(coupon, user, quantity)

        return coupon

    def get_lucky_number(self, obj):
        numbers = LuckyNumber.objects.filter(coupon=obj)
        return LuckyNumberOnlySerializer(numbers, many=True).data


    def get_products(self, obj):
        pivos = Pivo.objects.filter(coupon=obj)
        return [{"product_name": p.product.product_name, "quantity": p.quantity} for p in pivos]
