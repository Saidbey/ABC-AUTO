from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from apps.company.model.address import Address
from apps.company.serializer.address import AddressSerializer


class AddressViewSets(viewsets.ModelViewSet):
    queryset = Address.objects.order_by('id')
    serializer_class = AddressSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']


