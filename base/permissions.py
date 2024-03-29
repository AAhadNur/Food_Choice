
from rest_framework import permissions


class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to allow only admin users or the owner to delete or update an object.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD, or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to admin users who are also the owner of the object.
        return request.user.user_type == 'administrator' and obj.managing_admin == request.user


class IsEmployee(permissions.BasePermission):
    """
    Custom permission to allow only employee-type users to perform an action.
    """

    def has_permission(self, request, view):
        return request.user.profile.user_type == 'employee'


class IsAdministrator(permissions.BasePermission):
    """
    Custom permission to allow only administrator-type users to perform an action
    """

    def has_permission(self, request, view):
        return request.user.profile.user_type == 'administrator'
