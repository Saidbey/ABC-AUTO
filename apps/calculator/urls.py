from django.urls import path, include
from apps.shared.rest_framework.router import OptionalSlashRouter

from apps.calculator.views import CridetViewSet, PaymentViewSet, calculate

router = OptionalSlashRouter()

router.register('cridet', CridetViewSet, 'cridet')
router.register('payment', PaymentViewSet, 'payment')

urlpatterns = [
    path('', include(router.urls)),
    path('calculating/', calculate, name='calculate')
]
