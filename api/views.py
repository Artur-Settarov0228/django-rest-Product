from rest_framework import viewsets, filters
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductFilters
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = ProductFilters

    search_fields = ['name', 'category']

    ordering_fields = ['price', 'stock', 'created_at']
