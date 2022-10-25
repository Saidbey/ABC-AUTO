from django_filters import rest_framework as filters
from apps.automobile.models import Car


class CarFilter(filters.FilterSet):
    minimum_cost = filters.NumberFilter(field_name="cost_from", lookup_expr='gte')
    maximum_cost = filters.NumberFilter(field_name="cost_from", lookup_expr='lte')

    class Meta:
        model = Car
        fields = ['color', 'cost_from']
