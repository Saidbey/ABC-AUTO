from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

# Project
from apps.automobile.models.gifts import Gifts
from apps.automobile.serializers.gifts import BonusSerializer


class BonusViewSet(viewsets.ModelViewSet):
    queryset = Gifts.objects.order_by('id')
    serializer_class = BonusSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']