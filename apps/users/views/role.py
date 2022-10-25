from django.contrib.auth.models import Group, Permission
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.parsers import FormParser, MultiPartParser

from apps.users.models.role import Role
from apps.users.serializers.role import RoleModelSerializer, PermissionSerializer, GroupModelSerializer


class GroupViewSet(ModelViewSet):
    model = Group
    queryset = Group.objects.all()
    serializer_class = GroupModelSerializer
    search_fields = ['name']
    http_method_names = ['get', 'post', 'head']


class PermissionViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin,
                        GenericViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.filter(codename__startswith='view')
    lookup_field = 'pk'
    lookup_url_kwarg = 'pk'
    search_fields = ['name']
    http_method_names = ['get', 'post', 'head']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = Permission.objects.filter(user=self.request.user)
        else:
            queryset = Permission.objects.none()
        return queryset

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        if self.action == 'retrieve':
            perm = super(PermissionViewSet, self).get_permissions()
            return perm
        return super().get_permissions()


class RoleViewSet(viewsets.ModelViewSet):
    model = Role
    queryset = Role.objects.all()
    serializer_class = RoleModelSerializer
    search_fields = ['name']
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny()]
        return super().get_permissions()
