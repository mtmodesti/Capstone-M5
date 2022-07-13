from rest_framework import permissions

class isSuperuserOrCreateOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    