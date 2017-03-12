import django_filters
from ip_parse.models import CompromizedIP


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')


    class Meta:
        model = CompromizedIP
        fields = ['ip_adress', 'resourse', 'appear_date']