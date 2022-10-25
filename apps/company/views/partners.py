from rest_framework import viewsets

# projects
from apps.company.model.partners import Partners
from apps.company.serializer.partners import PartnersSerializer


class PartnersViewSets(viewsets.ModelViewSet):
    queryset = Partners.objects.order_by('id')
    serializer_class = PartnersSerializer
    http_method_names = ['get', 'post', 'delete', 'head']