from rest_framework import generics, permissions
from .models import CupomFiscal
from .serializers import CupomFiscalSerializer

class CupomFiscalCreateView(generics.CreateAPIView):
    queryset = CupomFiscal.objects.all()
    serializer_class = CupomFiscalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
