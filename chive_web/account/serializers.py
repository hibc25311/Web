from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=6,
        max_length=128,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
