from rest_framework import serializers
<<<<<<< HEAD
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
        num_str = str(obj.number).zfill(7)
       
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
=======
from .models import CupomFiscal
from num_sorte.models import NumeroSorte

class NumeroSorteSerializer(serializers.ModelSerializer):
    lote_serie = serializers.ReadOnlyField()  # usa a propriedade do model

    class Meta:
        model = NumeroSorte
        fields = ['numero', 'lote_serie']

class CupomFiscalSerializer(serializers.ModelSerializer):
    numeros_sorte = serializers.SerializerMethodField()  # adiciona o campo

    class Meta:
        model = CupomFiscal
        fields = ['id', 'usuario', 'cnpj', 'imagem', 'titulo_produto', 'quantidade', 'data_cadastro', 'numeros_sorte']
        read_only_fields = ['usuario', 'data_cadastro', 'numeros_sorte']

    def get_numeros_sorte(self, obj):
        numeros = NumeroSorte.objects.filter(cupom_fiscal=obj)  # usa o campo correto do model
        return NumeroSorteSerializer(numeros, many=True).data
>>>>>>> 43286f0 (pegar so o cupom e o numero)
