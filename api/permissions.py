from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


class IsAuthorAdminModeratorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return not request.user.is_anonymous()
        if request.method in ("PATCH", "DELETE"):
            return (
                request.user == obj.author
                or request.user.is_admin()
                or request.user.is_moderator()
            )
        if request.method in permissions.SAFE_METHODS:
            return True
        return False
