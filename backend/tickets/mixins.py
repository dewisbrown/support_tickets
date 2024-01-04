from rest_framework import permissions

from .permissions import IsStaffEditorPermission


class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser,
        IsStaffEditorPermission,
    ]


class UserQuerySetMixin():
    """
    Provides custom get_queryset function to filter by user.
    """
    owner_field = 'owner'
    def get_queryset(self, *args, **kwargs):
        # staff can view all tickets
        if self.request.user.is_staff:
            return super().get_queryset(*args, **kwargs)
        
        # filter by request user if not staff
        lookup_data = {}
        lookup_data[self.owner_field] = self.request.user
        qs = super().get_queryset(*args, **kwargs)
        return qs.filter(**lookup_data)
