from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnFeed(permissions.BasePermission):
    """Allow user to edit only their own feed"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""

        if request.method in permissions.SAFE_METHODS: #create new feed / view feed
            return True
        return obj.user_profile.id == request.user.id  # Update their own Feed