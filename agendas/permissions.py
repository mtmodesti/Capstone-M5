from rest_framework import permissions


class isSuperUserOrStaffOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            if obj.medico == request.user:
                return True
            if request.user.is_staff:
                return True

        if request.user.is_superuser:
            return True

        return False
