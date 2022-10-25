from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.company.views.about import AboutCompanyViewSets, FilialViewSets
from apps.company.views.address import AddressViewSets
from apps.company.views.partners import PartnersViewSets
router = DefaultRouter()

router.register('about', AboutCompanyViewSets, 'about')
router.register('filial', FilialViewSets, 'filial')
router.register('address', AddressViewSets, 'address')
router.register('partners', PartnersViewSets, 'partners')

urlpatterns = [
    path('', include(router.urls))
]
