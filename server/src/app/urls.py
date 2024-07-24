from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from .views.user_view import UserViewSet
from .views.admin_view import AdminViewSet
from .views.task_view import TaskViewSet

router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'admins', AdminViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='TaskApp API')),
]