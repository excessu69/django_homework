from django_filters import rest_framework as filters
from .models import Advertisement

from .models import AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter()
    status = filters.ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    creator = filters.NumberFilter(field_name='creator', lookup_expr='exact')

    class Meta:
        model = Advertisement
        fields = ['status', 'created_at']
