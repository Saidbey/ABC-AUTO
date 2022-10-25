# DRF
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser, MultiPartParser

# Projects
from apps.calculator.models import Cridet
from apps.calculator.serializers import CridetModelSezializer


class CridetViewSet(viewsets.ModelViewSet):
    queryset = Cridet.objects.order_by('id')
    serializer_class = CridetModelSezializer
    parser_classes = (FormParser, MultiPartParser)
    filter_backends = [DjangoFilterBackend]
    http_method_names = ['get', 'post', 'delete', 'head']
