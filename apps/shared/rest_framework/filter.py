from django_filters.rest_framework import FilterSet, CharFilter, DateFilter

from apps.shared.utils.helpers import is_int


class BaseFilter(FilterSet):
    ids = CharFilter(method='get_ids')
    start_date = DateFilter(field_name='created_date', lookup_expr='date__gte')
    end_date = DateFilter(field_name='created_date', lookup_expr='date__lte')

    def get_ids(self, queryset, name, value: str):
        value_list = value.split('-')
        if all(is_int(val) for val in value_list):
            return queryset.filter(id__in=value_list)
        return queryset
