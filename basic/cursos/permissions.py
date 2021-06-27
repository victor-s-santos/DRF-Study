from rest_framework import permissions


class EhSuperUser(permissions.BasePermission):

    def has_permission(self, request, view):
        """Allow delete method only to superuser"""
        if request.method == 'DELETE':
            if request.user.is_superuser:
                return True
            return False
        return True