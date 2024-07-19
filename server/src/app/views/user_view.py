from rest_framework import viewsets
from ..serializers.user_serializer import UserSerializer
from ..models.user_model import User

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer