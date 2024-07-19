from rest_framework import viewsets
from ..serializers.admin_serializer import AdminSerializer
from ..models.admin_model import Admin

class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer