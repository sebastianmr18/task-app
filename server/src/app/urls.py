from django.urls import path, include
from rest_framework import routers
from .views.user_view import UserViewSet
from .views.admin_view import AdminViewSet
from .views.task_view import TaskViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]