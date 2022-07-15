from rest_framework import permissions


class isSuperuserOrStaff(permissions.BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        if request.user.is_superuser or request.user.is_staff:
            if request.method == "DELETE":
                if request.user.is_superuser:
                    return True
                else:
                    return False
            return True

        return False
