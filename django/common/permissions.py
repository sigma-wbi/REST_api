from rest_framework import permissions


class IsUserOrStaff(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            return (obj == request.user) or request.user.is_staff
