from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import transaction
from rest_framework.exceptions import ValidationError
from ..models.user_model import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'birth_date', 'date_joined', 'password')
        extra_kwargs = {'password': {'write_only': True}}
        
    @transaction.atomic
    def create(self, validated_data):
        password = validated_data.pop('password', None)

        try:
            user = User.objects.create(**validated_data)
            if password is not None:
                user.set_password(password)

            user.save()
            return user

        except Exception as exception:
            raise ValidationError({type(exception).__name__: str(exception)})
        