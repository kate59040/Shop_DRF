import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    price_after = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_before = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = {
            'category__name': ['icontains'],
            'available': ['icontains'],
        }
