from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.siteconfig.views.banner import BannerViewSets
from apps.siteconfig.views.menubar import MenuBarViewSets

router = DefaultRouter()

router.register('banners', BannerViewSets, 'banners')
router.register('menubar', MenuBarViewSets, 'menubar')

urlpatterns = [
    path('', include(router.urls))
]
