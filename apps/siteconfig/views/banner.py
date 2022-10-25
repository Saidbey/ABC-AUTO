from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

# projects
from apps.siteconfig.model.banner import Banner
from apps.siteconfig.serializer.banner import BannerSerializer


class BannerViewSets(viewsets.ModelViewSet):
    queryset = Banner.objects.order_by('?')
    serializer_class = BannerSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']