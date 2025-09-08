
from django.urls import path
from .views import FiscalCouponCreateView, MyFiscalCouponView,ProductView

urlpatterns = [
    path('create/', FiscalCouponCreateView.as_view(), name='create_coupon'),
    path('myCoupon/', MyFiscalCouponView.as_view(), name='See_coupon'),
    path('products/', ProductView.as_view(), name = 'See_product')
]
