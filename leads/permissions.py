from rest_framework.permissions import BasePermission

class CompanyOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_company