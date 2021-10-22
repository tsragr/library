import django_filters
from .models import Book


class BookFilter(django_filters.FilterSet):
    date = django_filters.NumberFilter()
    date__gt = django_filters.NumberFilter(field_name='date', lookup_expr='gt')
    date__lt = django_filters.NumberFilter(field_name='date', lookup_expr='lt')
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ('author', 'title', 'date', 'date__gt', 'date__lt')
