from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed for all requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only allowed to owner of ticket
        return obj.owner == request.user


class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    """
    Custom permission to allow staff users to make view, change, and add tickets.
    """
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        """
        Checks if user is staff.
        """
        if not request.user.is_staff:
            return False
        return super().has_permission(request, view)

    # def has_permission(self, request, view):
    #     user = request.user
    #     print(user.get_all_permissions())
    #     if user.is_staff:
    #         if user.has_perm("tickets.add_ticket"): # "app-name.verb_model-name"
    #             return True
    #         if user.has_perm("tickets.delete_ticket"):
    #             return True
    #         if user.has_perm("tickets.change_ticket"):
    #             return True
    #         if user.has_perm("tickets.view_ticket"):
    #             return True
    #         return False
    #     return False
