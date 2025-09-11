from rest_framework import generics, permissions
from .models import FiscalCoupon, Pivo , Product
from .serializers import FiscalCouponSerializer ,ProductsSerializer
from num_sorte.utils import generate_numbers_for_coupon
from num_sorte.models import LuckyNumber
from cupom_fiscal.models import FiscalCoupon
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class FiscalCouponCreateView(generics.CreateAPIView):
    queryset = FiscalCoupon.objects.all()
    serializer_class = FiscalCouponSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        coupon = serializer.save()
      
        quantity = sum(p.quantity for p in coupon.pivo_set.all())
        generate_numbers_for_coupon(coupon, self.request.user,quantity)


class MyFiscalCouponView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cupons = FiscalCoupon.objects.filter(user_fk=request.user)
        serializer = FiscalCouponSerializer(cupons, many=True)
        return Response(serializer.data)


class ProductView(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductsSerializer(products,many=True)
        return Response(serializer.data)