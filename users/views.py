from rest_framework import generics
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserRegisterSerializer, UserLoginSerializer, MydataSerializer

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



class MydataView(generics.ListAPIView):

    serializer_class = MydataSerializer

    queryset = CustomUser.objects.all()
    serializer_class = MydataSerializer