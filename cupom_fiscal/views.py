from rest_framework import generics, permissions
from .models import CupomFiscal
from .serializers import CupomFiscalSerializer
from num_sorte.utils import generate_numeros_para_cupom 
from num_sorte.models import NumeroSorte
from cupom_fiscal.models import CupomFiscal 




class CupomFiscalCreateView(generics.CreateAPIView):
    queryset = CupomFiscal.objects.all()
    serializer_class = CupomFiscalSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        cupom = serializer.save(usuario=self.request.user)
      
        quantidade = cupom.quantidade
        generate_numeros_para_cupom(cupom, self.request.user, quantidade)
