from .user_serializer import UserSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.db import transaction
from ..models.user_model import User
from ..models.admin_model import Admin


class AdminSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email', read_only=True)
    
    first_name = serializers.CharField(source='user.first_name', read_only=True)
    
    last_name = serializers.CharField(source='user.last_name', read_only=True)
    
    is_active = serializers.BooleanField(source='user.is_active', read_only=True)
    
    is_staff = serializers.BooleanField(source='user.is_staff', read_only=True)
    
    is_superuser = serializers.BooleanField(source='user.is_superuser', read_only=True)
    
    birth_date = serializers.DateField(source='user.birth_date', read_only=True)
    
    date_joined = serializers.DateTimeField(source='user.date_joined', read_only=True)
    
    password = serializers.CharField(source='user.password', allow_blank=True, allow_null=True, write_only=True, required=False)
    
    class Meta(UserSerializer.Meta):
        model = Admin
        fields = UserSerializer.Meta.fields + ('role',)
        
    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        
        try:
            user = User.objects.get(user_email=user_data['user_email'])
            
            admin = Admin.objects.create(user=user, **validated_data)
            return admin
        except Exception as exception:
            raise ValidationError({type(exception).__name__: str(exception)})