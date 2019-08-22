from rest_framework.permissions import BasePermission
from .exceptions import NotAdminException, NotOwnerException

class IsOwner(BasePermission):
    message = 'User is not Owner'
    def has_object_permission(self, request, view, obj):
        print('IsOwner Permission checker')
        print(obj.uid)
        print(request.user.uid)
        return obj.uid == request.user.uid
        # raise NotAdminException()

class IsAdmin(BasePermission):
    message = 'Not Admin'
    def has_permission(self, request, view):
        print('IsAdmin Permission checker')
        return request.user.is_admin()

class IsOwnerOrAdmin(BasePermission):
    message = 'Custom Message'

    def has_object_permission(self, request, view, obj):
        return obj.uid == request.user.uid or request.user.is_admin()
