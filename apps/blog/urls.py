from rest_framework.routers import DefaultRouter
from django.urls import path, include

# project
from apps.blog.view import NewsViewSets, CommentViewSets

router = DefaultRouter()

router.register('news', NewsViewSets, 'news')
router.register('comments', CommentViewSets, 'comment')

urlpatterns = [
    path('', include(router.urls))
]
