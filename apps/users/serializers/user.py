from collections import defaultdict

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

from apps.users.models import User
from django.contrib.auth.password_validation import validate_password


class CheckTokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)


class UserIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
        ]


class UserClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
        ]


class UserUpdateDataSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'is_superuser',
            'language',
            'theme',
            'password',
        ]

    def validate(self, attrs):
        if password := attrs.get('password'):
            attrs['password'] = make_password(password)
        return attrs


class UserDataSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, validators=[validate_password])

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'email',
            'phone_number',
            'is_superuser',
            'language',
            'theme',
            'password',
        ]

    def validate(self, attrs):
        if password := attrs.get('password'):
            attrs['password'] = make_password(password)
        return attrs


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user_data'] = UserDataSerializer(self.user).data

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)

        return data


class UserModelSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, required=False,
                                     write_only=True)
    # role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = dict(
            password=dict(required=True),
        )

    def validate(self, attrs):
        errors = defaultdict(list)
        users = User.objects.filter(username=attrs['username'])

        if self.instance:
            users = users.exclude(pk=self.instance.id)
        if users.exists():
            errors['username'].append('Username has already taken')
        if errors:
            raise serializers.ValidationError(errors)
        return attrs

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = super().create(validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        return representation
