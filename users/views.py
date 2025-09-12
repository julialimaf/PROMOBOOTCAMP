from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserLoginSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from projetobootcamp.utils_cache import get_cache, set_cache, delete_cache
from django.shortcuts import render

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegisterSerializer

class LoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        refresh = RefreshToken.for_user(user)
        return Response({
            "cpf": user.cpf,
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        })


class MyDataView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        cache_key = f"user_{request.user.id}_data"
        data = get_cache(cache_key)

        if data is None:
            serializer = UserRegisterSerializer(request.user)
            data = serializer.data
            set_cache(cache_key, data, timeout=300)
        return Response(data)





def welcome_page(request):
   
    if request.user.is_authenticated:
        
        email = request.user.email
    else:
        
        email = "Visitor"

    
    context = {
        'email': email,
    }

   
    return render(request, 'welcome.html', context)