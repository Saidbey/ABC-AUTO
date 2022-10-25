from rest_framework.permissions import BasePermission


class Ruxsatnoma(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.username == "Admin")
