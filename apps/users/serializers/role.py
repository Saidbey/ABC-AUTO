from rest_framework import serializers
from django.contrib.auth.models import Group

from apps.users.models.role import Role


class PermissionSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    codename = serializers.ReadOnlyField()


class GroupSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()
    permissions = PermissionSerializer(many=True, read_only=True)


class PositionSelectSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    name = serializers.ReadOnlyField()


class RoleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'id',
            'name',
            'groups',
        ]

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        users = instance.user.all()
        groups = instance.groups.all()
        for user in users:
            user.groups.set(list(groups))
        return instance

    def to_representation(self, instance):
        self.fields['groups'] = GroupSerializer(many=True)
        return super().to_representation(instance)


class GroupModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'permissions'
        ]

    def to_representation(self, instance):
        self.fields['permissions'] = PermissionSerializer(many=True,
                                                          read_only=True)
        return super().to_representation(instance)
