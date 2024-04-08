from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['pk', 'email', 'password', 'JWTToken']

    def create(self, validated_data):
        password = validated_data.pop('password')
        instance = super().create(validated_data)
        instance.set_password(password)
        instance.save()
        return instance


class AuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email', 'password']


class PasswordRecoverySerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['pk', 'password']


class RequestPasswordRecoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'email']
