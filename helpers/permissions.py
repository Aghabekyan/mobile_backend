from rest_framework.permissions import BasePermission
from .exceptions import NotAdminException

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        print('IsOwner Permission checker')
        return True

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        print('IsAdmin Permission checker')
        if request.user.role.id == 1:
            return True
        raise NotAdminException()

class IsTest(BasePermission):
    def has_permission(self, request, view):
        print('IsTest Permission checker')
        if request.user.role.id == 1:
            return True
        raise NotAdminException()
