from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from apps.siteconfig.model.menubar import MenuBar
from apps.siteconfig.serializer.menubar import MenyBarSerializer


class MenuBarViewSets(viewsets.ModelViewSet):
    queryset = MenuBar.objects.order_by('id')
    serializer_class = MenyBarSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']