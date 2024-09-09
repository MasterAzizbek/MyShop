from rest_framework import serializers
from .models import UserModel


class UserSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        user = UserModel.objects.create_user(**validated_data)
        return user

    class Meta:
        model = UserModel
        fields = ('email', 'password',)
        
