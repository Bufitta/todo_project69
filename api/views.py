import os
from rest_framework import viewsets
from .serializers import CategorySerializer, TaskSerializer, UserSerializer, AttachmentSerializer
from tasks.models import Category, Task, Attachment, User
from django.shortcuts import get_object_or_404
from django.conf import settings
from .permissions import IsAuthor
from rest_framework.decorators import action
from django.http import FileResponse


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.request.user.tasks.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=['get'], detail=False)
    def download(self, request):
        tasks = self.request.user.tasks.all()
        text = '\n'.join([f'{task.title} {task.deadline} ' for task in tasks])
        return FileResponse(
            text,
            content_type='text/plain',
            filename='my_tasks.txt'
        )


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'username'


class AttachmentViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentSerializer
    permission_classes = [IsAuthor]

    def get_queryset(self):
        task = get_object_or_404(Task, id=self.kwargs.get('task_id'))
        return task.attachments.all()

    def perform_create(self, serializer):
        task = get_object_or_404(Task, id=self.kwargs.get('task_id'))
        serializer.save(task=task)

    def perform_destroy(self, instance):
        filepath = f'{settings.MEDIA_ROOT}/{instance.file.name}'
        if os.path.exists(filepath):
            os.remove(filepath)
        instance.delete()
