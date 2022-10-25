from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser

# Project
from apps.automobile.models import Car, PositionCategory
from apps.automobile.serializers import CarModelSerializer, ComparePositionSerializer
# from automobile.filters.car import CarFilter


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.order_by('id')
    serializer_class = CarModelSerializer
    parser_classes = (FormParser, MultiPartParser)
    filter_backends = [DjangoFilterBackend, SearchFilter]
    http_method_names = ['get', 'post', 'delete', 'head']
    # search_fields = ['title', 'type', 'color', 'cost_from', 'is_active']
    # filter_class = CarFilter
    # filterset_fields = ['type', 'color', 'cost_from']

    @action(['GET'], detail=True, serializer_class=ComparePositionSerializer)
    def compare(self, request, pk=None):
        compared = PositionCategory.objects.filter(car_id=pk)
        serializer = self.serializer_class(compared, many=True)
        return Response(serializer.data)
