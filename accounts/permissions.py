from rest_framework.permissions import BasePermission,


class IsUserOwner(BasePermission):
    """
    Custom Permission checking if the user owns the account they're accessing
    """

    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsAccountOwner(BasePermission):
    """
    Custom Permission checking if the user owns the Account Object.
    """

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsTransactionOwner(BasePermission):
    """
    Custom Permission checking if the user owns the Transaction Object.
    """

    def has_object_permission(self, request, view, obj):
        return obj.account.owner == request.user
