
from rest_framework import viewsets
from .models import LuckyNumber, LuckyNumberControl
from .serializers import LuckyNumberSerializer

class LuckyNumberView(viewsets.ModelViewSet):
    queryset = LuckyNumber.objects.all()
    serializer_class = LuckyNumberSerializer


