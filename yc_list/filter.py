import django_filters
from django.db.models import Q
from .models import    YcListViews

class BooksFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = YcListViews
        # fileds = ('id','gtitle','gcontext','gpic')
        fields = '__all__'