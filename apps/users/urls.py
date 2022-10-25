# Django
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

# Project
from apps.users.views.auth import AuthViewSet, LoginView
from apps.users.views.user import UserViewSet
from apps.users.views import RoleViewSet, GroupViewSet, PermissionViewSet
from apps.users.views import CustomerViewSets

router = DefaultRouter()
router.register('auth', AuthViewSet, 'auth')
router.register('users', UserViewSet, 'users')
router.register('roles', RoleViewSet, 'roles')
router.register('groups', GroupViewSet, 'groups')
router.register('permissions', PermissionViewSet, 'permissions')
router.register('customer', CustomerViewSets, 'customer')

urlpatterns = [
    path('login/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('login', LoginView.as_view(), name='login'),
    path('', include(router.urls)),

]
