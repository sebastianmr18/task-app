from rest_framework import viewsets
from ..serializers.task_serializer import TaskSerializer
from ..models.task_model import Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer