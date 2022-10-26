from django.urls import path, include
from rest_framework.routers import DefaultRouter


from apps.automobile.views import CarViewSet, PositionCategoryViewSet
from apps.automobile.views.gifts import BonusViewSet
from apps.automobile.views.company import CompanyViewSet
from apps.automobile.views.usedcars import UsedCarsViewSets

router = DefaultRouter()

router.register('car', CarViewSet, 'car')
router.register('company', CompanyViewSet, 'company')
router.register('bonus', BonusViewSet, 'bonus')
router.register('position-category', PositionCategoryViewSet, 'position-category')
router.register('usedcars', UsedCarsViewSets, 'usedcars')

urlpatterns = [
    path('', include(router.urls))
]