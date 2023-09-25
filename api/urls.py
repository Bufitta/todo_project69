from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, TaskViewSet, UserViewSet, AttachmentViewSet

app_name = 'api'

v1_router = DefaultRouter()

v1_router.register(r'categories', CategoryViewSet)
v1_router.register(r'tasks', TaskViewSet, basename='task')
v1_router.register(r'users', UserViewSet)
# v1_router.register('attachments', AttachmentViewSet)
v1_router.register(r'tasks/(?P<task_id>\d+)/attachments', AttachmentViewSet, basename='attachment')

urlpatterns = [path('v1/', include(v1_router.urls))]

