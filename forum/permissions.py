from rest_framework import permissions
from rest_framework.request import Request


class IsOwnerOfObjectOrRead(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        else:
            return obj.user == request.user


class CategoryPermission(permissions.BasePermission):
    def has_permission(self, request, view):

        if request.method == "GET":
            return True
        else:
            if view.action == "posts_for_category":
                return request.user.is_authenticated
            return request.user.is_superuser

    


