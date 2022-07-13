from rest_framework import permissions

class isSuperUser(permissions.IsAdminUser):
    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:

            if request.user.is_staff:

                return True

        if request.user.is_superuser:

            return True

        return False