from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from apps.automobile.models.usedcars import Usedcars
from apps.automobile.serializers.usedcars import UsedCarsSerializer


class UsedCarsViewSets(viewsets.ModelViewSet):
    queryset = Usedcars.objects.order_by('id')
    serializer_class = UsedCarsSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']
