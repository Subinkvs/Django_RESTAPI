from rest_framework import permissions

class IsStaffEditorPermission(permissions.DjangoModelPermissions):
    def has_permission(self, request, view):
        user = request.user
        print(user.get_all_permissions())
        if user.is_staff:
            if user.has_perm("product.view_Product"):
                return True
            if user.has_perm("product.change_Product"):
                return True
            if user.has_perm("product.add_Product"):
                return True
            if user.has_perm("product.delete_Product"):
                return True
            return False
        return False
    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
        