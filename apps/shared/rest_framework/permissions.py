from rest_framework.permissions import BasePermission, DjangoModelPermissions


class IsSaveMethod(BasePermission):
    save_methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', 'OPTIONS', ]

    def has_permission(self, request, view):
        return request.method in self.save_methods


class IsAuthenticated(IsSaveMethod):

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and
                super(IsAuthenticated, self).has_permission(request, view))


class CustomDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.add_%(model_name)s']
