from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from apps.users.models.customer import Customer
from apps.users.serializers.customer import CustomerSerializer


class CustomerViewSets(viewsets.ModelViewSet):
    queryset = Customer.objects.order_by('id')
    serializer_class = CustomerSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']