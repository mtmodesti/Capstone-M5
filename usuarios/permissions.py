from rest_framework import permissions
from rest_framework.permissions import BasePermission, SAFE_METHODS


class isSuperUser(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)


class isSuperUserOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if bool(request.user and request.user.is_superuser):
            return True
        return request.user == obj



class isSuperUserOrStaff(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and (request.user.is_superuser or request.user.is_staff) )
