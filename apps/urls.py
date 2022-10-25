from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('users/', include(('users.urls', 'users'), 'users')),
    path('company/', include(('company.urls', 'company'), 'company')),
    path('automobile/', include(('automobile.urls', 'automobile'), 'automobile')),
    path('calculator/', include(('calculator.urls', 'calculator'), 'calculator')),
    path('blog/', include(('blog.urls', 'blog'), 'blog')),
    path('siteconfig/', include(('siteconfig.urls', 'siteconfig'), 'siteconfig')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
