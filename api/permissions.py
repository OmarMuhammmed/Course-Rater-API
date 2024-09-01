from rest_framework import permissions

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object or admin to edit it.
    """
    def has_object_permission(self, request, view, obj):

        if request.user.is_staff:
            return True
        
        # Allow users to edit their own profile
        return obj == request.user
    