from django.urls import path
from .views import CupomFiscalCreateView

urlpatterns = [
    path('criar/', CupomFiscalCreateView.as_view(), name='criar_cupom'),
]
