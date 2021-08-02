import django_filters
from .models import *

class StdFilter (django_filters.FilterSet):
    class Meta:
        model = App1Students
        fields = '__all__'