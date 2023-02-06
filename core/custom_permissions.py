from rest_framework.permissions import IsAuthenticated


GROUPS = [
    'admin',
]


class IsAdminPermissions(IsAuthenticated):
    def has_permission(self, request, view):
        default = super().has_permission(request, view)
        if default and request.user.groups.filter(name=GROUPS[0]).exists():
            return True
        return False

