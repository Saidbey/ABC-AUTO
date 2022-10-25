from rest_framework.viewsets import ModelViewSet

from apps.users.models import User
from apps.users.serializers.user import UserModelSerializer
from rest_framework.parsers import FormParser, MultiPartParser


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']

    queryset = User.objects.all()
    ordering = ['-date_joined']
    search_fields = ['username']
