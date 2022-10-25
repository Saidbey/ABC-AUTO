from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

# projects
from apps.blog.model.news import News
from apps.blog.serializer.news import NewsSerializer


class NewsViewSets(viewsets.ModelViewSet):
    queryset = News.objects.order_by('id')
    serializer_class = NewsSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']