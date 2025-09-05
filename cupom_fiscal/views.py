from rest_framework import generics, permissions
from .models import FiscalCoupon
from .serializers import FiscalCouponSerializer
from num_sorte.utils import generate_numbers_for_coupon
from num_sorte.models import LuckyNumber
from cupom_fiscal.models import FiscalCoupon




class FiscalCouponCreateView(generics.CreateAPIView):
    queryset = FiscalCoupon.objects.all()
    serializer_class = FiscalCouponSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        coupon = serializer.save(user=self.request.user)
      
        quantity = coupon.quantity 
        generate_numbers_for_coupon(coupon, self.request.user,quantity)
