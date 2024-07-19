from rest_framework import serializers
from ..models.task_model import Task
from django.db import transaction

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'description', 'created_at', 'updated_at', 'is_complete', 'is_important')
        read_only_fields = ('id', 'created_at', 'updated_at')
        
    @transaction.atomic
    def create(self, validated_data):
        task = Task.objects.create(**validated_data)
        return task