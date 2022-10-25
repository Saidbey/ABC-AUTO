from rest_framework import permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.shared.rest_framework.permissions import IsAuthenticated
from apps.users.models import User
from apps.users.serializers.user import MyTokenObtainPairSerializer


class AuthViewSet(GenericViewSet):
    serializer_class = AuthTokenSerializer
    queryset = User.objects.all()
    http_method_names = ['get', 'post', 'head']

    @action(['POST'], detail=False, permission_classes=[permissions.AllowAny])
    def login(self, request: Request):
        self.serializer_class = AuthTokenSerializer
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['username']
        # password = serializer.validated_data['username']
        token, created = Token.objects.get_or_create(user=user, )
        return Response({'token': token.key})

    @action(['DELETE'], detail=False, permission_classes=[IsAuthenticated])
    def logout(self, request: Request):
        Token.objects.get(user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(TokenObtainPairView):
    permission_classes = [IsAuthenticated]
    serializer_class = MyTokenObtainPairSerializer
    http_method_names = ['get', 'post', 'delete', 'head']
