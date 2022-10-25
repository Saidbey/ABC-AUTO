from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from apps.company.model.about import AboutCompany, Filials
from apps.company.serializer.about import AboutCompanySerializer, FilialSerializer


class AboutCompanyViewSets(viewsets.ModelViewSet):
    queryset = AboutCompany.objects.order_by('id')
    serializer_class = AboutCompanySerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'head']


class FilialViewSets(viewsets.ModelViewSet):
    queryset = Filials.objects.order_by('id')
    serializer_class = FilialSerializer
    parser_classes = (FormParser, MultiPartParser)
    http_method_names = ['get', 'post', 'delete', 'head']
