from rest_framework import serializers
from django.contrib.auth import authenticate, password_validation
from django.core import exceptions
from .models import CustomUser
from users.services import send_email


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('cpf', 'first_name', 'last_name', 'email', 'password','telefone',
                  'endereco_estado', 'endereco_cidade', 'endereco_cep')

        def validate_password(self, value):
                                                    
            try:
                password_validation.validate_password(value, self.instance)
            except exceptions.ValidationError as e:
                raise serializers.ValidationError(list(e.messages))
            return value


    def create(self, validated_data):
        password = validated_data.pop('password')
        cpf = validated_data.get('cpf')


        send_email(
            subjects='Bem-vindo a Promoção Bootcamp! ',    
            from_email= 'promobootcamp@catskillet.com',
            to_email=[validated_data.get('email')],
            template='welcome.html',
            context={'first_name': validated_data.get('first_name')},

        )


        user = CustomUser(**validated_data)
        user.username = cpf  
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    cpf = serializers.CharField()
    password = serializers.CharField(write_only=True) ######apenas para escrever, não sera visto (aula 25-08)

    def validate(self, attrs):
        cpf = attrs.get('cpf')
        password = attrs.get('password')
        user = authenticate(username=cpf, password=password)
        if not user:
            raise serializers.ValidationError('Credenciais inválidas')
        if not user.is_active:
            raise serializers.ValidationError('Conta desativada')
        return {'user': user}

class MydataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('cpf', 'first_name', 'last_name', 'email','telefone', 'endereco_estado', 'endereco_cidade', 'endereco_cep')