import django_filters 
from .models import Product

class ProductFilters(django_filters.FilterSet):
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    stock = django_filters.NumberFilter(field_name='stock', lookup_expr='gte')

    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Product
        fields = ['min_price', 'max_price', 'stock', 'created_at']

