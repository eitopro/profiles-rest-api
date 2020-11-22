from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        """Check if the user is trying to edit his own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        """ for non safe mothods:PUT, PATCH, and DELETE we return true if the user id match"""
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """check if the user is trying to update his own status"""
    def has_object_permission(self, request, view, obj):
        if request.method is permissions.SAFE_METHODS:
            return True
        
        """ for non safe mothods:PUT, PATCH, and DELETE we return true if the user id match"""
        return obj.user_profile.id == request.user.id

