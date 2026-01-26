from django.contrib.auth.models import User
from rest_framework import serializers

from apps.users.services import create_user


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "email", "password")

    def create(self, validated_data):
        return create_user(**validated_data)