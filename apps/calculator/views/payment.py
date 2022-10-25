# DRF
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.parsers import FormParser, MultiPartParser

# Projects
from apps.calculator.models import Payment, Cridet
from apps.calculator.serializers import PaymentModelSezializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.order_by('id')
    serializer_class = PaymentModelSezializer
    parser_classes = (FormParser, MultiPartParser)
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['credit']
    http_method_names = ['get', 'post', 'delete', 'head']
