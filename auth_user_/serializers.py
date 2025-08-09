from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import CustomUser
from django.core.validators import ValidationError
from rest_framework import  status
class RegisterSerializers(serializers.ModelSerializer):
    password=serializers.CharField(max_length=15)
    confirm_password=serializers.CharField(max_length=15)
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','age','address','password','confirm_password']


    def validate(self, data):
        if data.get['password']!=data.get['confirm_password']:
            raise ValidationError({'mesege':'Parolar mos emas','status':status.HTTP_400_BAD_REQUEST})
        username=data.get['username']
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError({'mesege':'Bu username orqali royhatan otilgan','status':status.HTTP_400_BAD_REQUEST})
        return data
    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user=CustomUser.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            age=validated_data['age'],
            address=validated_data['address']

        )
        user.set_password(validated_data['password'])
        user.save()
        Token.ibjects.create(user=user)

        return user
