from django.urls import path
from .views import FiscalCouponCreateView

urlpatterns = [
    path('create/', FiscalCouponCreateView.as_view(), name='create_coupon'),
]
