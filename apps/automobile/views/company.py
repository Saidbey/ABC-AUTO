from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

# Project
from apps.automobile.models.company import CarCompany
from apps.automobile.serializers.company import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = CarCompany.objects.order_by('id')
    serializer_class = CompanySerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']