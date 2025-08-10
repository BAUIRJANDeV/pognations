from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser
from rest_framework.validators import ValidationError
from rest_framework import status
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=128)
    confirm_password = serializers.CharField(write_only=True, max_length=128)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'age', 'address', 'password', 'confirm_password']

    def validate(self, data):
        if data.get('password') != data.get('confirm_password'):
            raise ValidationError({'message': 'Parollar mos emas', 'status': status.HTTP_400_BAD_REQUEST})

        username = data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError(
                {'message': 'Bu username orqali ro\'yxatdan o\'tilgan', 'status': status.HTTP_400_BAD_REQUEST})

        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        Token.objects.create(user=user)

        return user



class LoginSerializer(serializers.Serializer):
    username=serializers.CharField(max_length=120)
    password=serializers.CharField(max_length=120)

    def validate(self, data):
        if not data['username'] or not data['password']:
            raise ValidationError({'error':'Login yoki parol notogri','status':status.HTTP_400_BAD_REQUEST})
        try:
            authenticate(username=data['username'],password=data['password'])
            user=CustomUser.objects.get(username=data['username'])
            token,created=Token.objects.get_or_create(user=user)
        except Exception as e:
            raise ValidationError({'error':e,'status':status.HTTP_400_BAD_REQUEST})
        data['token']=token.key
        return data
