from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.task.user == request.user or request.method in SAFE_METHODS
