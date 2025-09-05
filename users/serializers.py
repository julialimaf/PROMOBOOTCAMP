from rest_framework import serializers
from django.contrib.auth import authenticate, password_validation
from django.core import exceptions
from .models import CustomUser
from users.services import send_email


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = (
            'cpf',
            'first_name',
            'last_name',
            'email',
            'password',
            'phone',
            'address_city',
            'address_state',
            'address_zip'
        )

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
            subject='Welcome to Promo Bootcamp!',
            from_email='promobootcamp@catskillet.com',
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
    password = serializers.CharField(write_only=True)  
    def validate(self, attrs):
        cpf = attrs.get('cpf')
        password = attrs.get('password')
        user = authenticate(username=cpf, password=password)
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_active:
            raise serializers.ValidationError('Account disabled')
        return {'user': user}


class MyDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'cpf',
            'first_name',
            'last_name',
            'email',
            'telefone',
            'endereco_estado',
            'endereco_cidade',
            'endereco_cep'
        )
